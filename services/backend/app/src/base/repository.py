import json

from math import ceil

from typing import TypeVar, Generic, List, Optional, Type, Any, Dict

from fastapi import HTTPException

from pydantic import ValidationError

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import selectinload
from sqlalchemy.sql import Select

from src.ports.repository import RepositoryPort
from src.ports.filtering import (
    FiltersInterface,
    OrderParams,
    PaginationParams,
    SearchParams,
    SearchOperator,
    OrderDirection,
)
from src.databases import engine
from src.base.model import CustomModel

T = TypeVar('T', bound=CustomModel)

BaseSchema = declarative_base()


class BaseRepository(RepositoryPort[T], Generic[T]):
    """Base repository class"""
    
    def __init__(
        self,
        model: Type[T],
        schema: Type[T]
    ):
        """..."""

        self.model = model
        self.schema = schema

    def _build_filter_condition(self, filter_condition: SearchParams | Dict[str, Any]) -> Any:
        """Build SQLAlchemy filter condition from SearchParams"""

        if isinstance(filter_condition, dict):
            try:
                filter_condition = SearchParams(
                    attribute=filter_condition['attribute'],
                    operator=filter_condition['operator'],
                    value=filter_condition.get('value', None)
                )
            except KeyError as exc:
                raise HTTPException(
                    status_code=400,
                    detail="Filter conditions must include attribute and operator"
                ) from exc

        attribute_name = filter_condition.attribute
        if not hasattr(self.schema, attribute_name):
            raise HTTPException(
                status_code=400,
                detail=f"Attribute '{attribute_name}' is not valid for {self.schema.__name__}"
            )

        attribute = getattr(self.schema, attribute_name)

        operator = filter_condition.operator

        if operator == SearchOperator.EQ:
            return attribute == filter_condition.value
        elif operator == SearchOperator.NE:
            return attribute != filter_condition.value
        elif operator == SearchOperator.GT:
            return attribute > filter_condition.value
        elif operator == SearchOperator.GTE:
            return attribute >= filter_condition.value
        elif operator == SearchOperator.LT:
            return attribute < filter_condition.value
        elif operator == SearchOperator.LTE:
            return attribute <= filter_condition.value
        elif operator == SearchOperator.LIKE:
            return attribute.like(filter_condition.value)
        elif operator == SearchOperator.ILIKE:
            return attribute.ilike(filter_condition.value)
        elif operator == SearchOperator.CONTAINS:
            return attribute.contains(filter_condition.value)
        elif operator == SearchOperator.ICONTAINS:
            pattern = f"%{filter_condition.value}%"
            return attribute.ilike(pattern)
        elif operator == SearchOperator.IN:
            return attribute.in_(filter_condition.value)
        elif operator == SearchOperator.NOT_IN:
            return ~attribute.in_(filter_condition.value)
        elif operator == SearchOperator.IS_NULL:
            return attribute.is_(None)
        elif operator == SearchOperator.IS_NOT_NULL:
            return attribute.is_not(None)
        else:
            raise HTTPException(
                status_code=400,
                detail=f"Unsupported operator: {operator}"
            )

    async def create(self, item: T) -> T:
        """Create a new item"""

        async with AsyncSession(engine) as session:

            item_data = item.model_dump(exclude_none=True)
            # Only keep attributes that belong to the target schema table
            try:
                table_columns = {col.name: col for col in self.schema.__table__.columns}
                filtered_data = {}
                # auto serialize dict/list into JSON strings when column is Text/String
                from sqlalchemy import Text, String
                for key, value in item_data.items():
                    if key not in table_columns:
                        continue
                    col = table_columns[key]
                    if isinstance(value, (dict, list)) and isinstance(col.type, (Text, String)):
                        filtered_data[key] = json.dumps(value)
                    else:
                        filtered_data[key] = value
            except Exception:
                filtered_data = item_data
            db_item = self.schema(**filtered_data)
            session.add(db_item)
            await session.commit()
            await session.refresh(db_item)
            
            # Merge back DB values with original model to keep required fields (e.g., name)
            try:
                db_columns = {col.name for col in self.schema.__table__.columns}
                db_data = {k: v for k, v in db_item.__dict__.items() if k in db_columns}
            except Exception:
                db_data = db_item.__dict__
            merged = {**item.model_dump(exclude_none=True), **db_data}
            return self.model.model_validate(merged)

    async def list(self, filters: Optional[Dict[Any, Any]] = None) -> Dict[str, Any]:
        """List all items with search, ordering and pagination."""

        filters_payload = self._normalize_filters(filters)
        async with AsyncSession(engine) as session:
            base_query = self._build_list_query(filters_payload.model_copy(deep=True))
            total_items = await self._count_results(session, base_query)
            pagination_meta, offset = self._build_pagination_metadata(
                filters_payload.pagination, total_items
            )
            ordered_query = self._apply_ordering(base_query, filters_payload.order)
            limited_query = ordered_query.offset(offset).limit(pagination_meta.num_items)

            result = await session.execute(limited_query)
            items = result.scalars().all()
            serialized_items = [self.model.model_validate(item.__dict__) for item in items]

            return {
                "items": serialized_items,
                "pagination": pagination_meta.model_dump(),
                "order": filters_payload.order.model_dump()
            }

    async def detail(
        self,
        pk: str,
        include_relations: Optional[List[str]] = None
    ) -> Optional[T]:
        """Get item by primary key"""
        
        async with AsyncSession(engine) as session:

            query = select(self.schema).where(
                getattr(self.schema, self.model.pk_field) == pk
            )
            
            if include_relations:
                for relation in include_relations:
                    if hasattr(self.schema, relation):
                        query = query.options(selectinload(getattr(self.schema, relation)))
            
            result = await session.execute(query)
            item = result.scalar_one_or_none()
            
            if not item:
                raise HTTPException(
                    status_code=404,
                    detail=f"{self.model.__name__} with pk: {pk} not found"
                )
            
            return self.model.model_validate(item.__dict__)

    async def update(self, pk: str, item_update: T) -> T:
        """Update an item"""
        
        async with AsyncSession(engine) as session:

            result = await session.execute(
                select(self.schema).where(
                    getattr(self.schema, self.model.pk_field) == pk
                )
            )
            item = result.scalar_one_or_none()
            
            if not item:
                raise HTTPException(
                    status_code=404,
                    detail=f"{self.model.__name__} with pk: {pk} not found"
                )
            
            item_data = item_update.model_dump(exclude_unset=True)
            # auto serialize dict/list into JSON strings when column is Text/String
            from sqlalchemy import Text, String
            table_columns = {col.name: col for col in self.schema.__table__.columns}

            for key, value in item_data.items():
                if key not in table_columns:
                    setattr(item, key, value)
                    continue
                col = table_columns[key]
                if isinstance(value, (dict, list)) and isinstance(col.type, (Text, String)):
                    setattr(item, key, json.dumps(value))
                else:
                    setattr(item, key, value)
            
            session.add(item)
            await session.commit()
            await session.refresh(item)
            
            return self.model.model_validate(item.__dict__)

    async def update_partial(self, pk: str, item_update: T) -> None:
        """Update an item without returning the validated model (for partial updates)"""
        
        async with AsyncSession(engine) as session:

            result = await session.execute(
                select(self.schema).where(
                    getattr(self.schema, self.model.pk_field) == pk
                )
            )
            item = result.scalar_one_or_none()
            
            if not item:
                raise HTTPException(
                    status_code=404,
                    detail=f"{self.model.__name__} with pk: {pk} not found"
                )
            
            item_data = item_update.model_dump(exclude_unset=True)
            # auto serialize dict/list into JSON strings when column is Text/String
            from sqlalchemy import Text, String
            table_columns = {col.name: col for col in self.schema.__table__.columns}

            for key, value in item_data.items():
                if key not in table_columns:
                    continue
                col = table_columns[key]
                if isinstance(value, (dict, list)) and isinstance(col.type, (Text, String)):
                    setattr(item, key, json.dumps(value))
                else:
                    setattr(item, key, value)
            
            session.add(item)
            await session.commit()
            await session.refresh(item)

    async def delete(self, pk: str) -> None:
        """Delete an item"""
        
        async with AsyncSession(engine) as session:
            result = await session.execute(
                select(self.schema).where(
                    getattr(self.schema, self.model.pk_field) == pk
                )
            )
            item = result.scalar_one_or_none()
            
            if not item:
                raise HTTPException(
                    status_code=404,
                    detail=f"{self.model.__name__} with pk: {pk} not found"
                )
            
            await session.delete(item)
            await session.commit()

    def _normalize_filters(self, filters: Optional[Any]) -> FiltersInterface:
        """Ensure filters are represented with the FiltersPayload model."""

        try:
            return FiltersInterface.from_raw(filters)
        except (ValueError, ValidationError) as exc:
            raise HTTPException(status_code=400, detail=str(exc)) from exc

    def _build_list_query(self, filters_payload: FiltersInterface) -> Select:
        """Create the base select statement for list queries."""

        query = select(self.schema)
        return self._apply_search_filters(query, filters_payload.search)

    def _apply_search_filters(self, query: Select, search_filters: List[SearchParams]) -> Select:
        """Apply search filters to the query."""

        if not search_filters:
            return query

        conditions = []
        for filter_condition in search_filters:
            conditions.append(self._build_filter_condition(filter_condition))

        if conditions:
            query = query.where(and_(*conditions))
        return query

    async def _count_results(self, session: AsyncSession, query: Select) -> int:
        count_query = select(func.count()).select_from(query.subquery())
        result = await session.execute(count_query)
        total = result.scalar()
        return int(total or 0)

    def _build_pagination_metadata(
        self,
        pagination: PaginationParams,
        total_items: int
    ) -> tuple[PaginationParams, int]:
        """Calculate pagination metadata and the required offset."""

        num_items = pagination.num_items
        max_page = ceil(total_items / num_items) if total_items else 1
        max_page = max(1, max_page)
        page = min(pagination.page, max_page)
        offset = (page - 1) * num_items

        return (
            PaginationParams(
                page=page,
                num_items=num_items,
                min_page=1,
                max_page=max_page,
                total_items=total_items
            ),
            offset
        )

    def _apply_ordering(self, query: Select, order: OrderParams) -> Select:
        """Apply ordering to the select query."""

        attribute = order.attribute
        if not hasattr(self.schema, attribute):
            raise HTTPException(
                status_code=400,
                detail=f"Order attribute '{attribute}' is not valid for {self.schema.__name__}"
            )

        column = getattr(self.schema, attribute)
        if order.direction == OrderDirection.DESC:
            return query.order_by(column.desc())
        return query.order_by(column.asc())
