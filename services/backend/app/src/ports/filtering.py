from __future__ import annotations

from typing import Any, Generic, List, Optional, TypeVar

from enum import Enum

from pydantic import BaseModel, Field, ValidationError, field_validator

T = TypeVar("T")


class SearchOperator(str, Enum):
    """Allowed operators for search filters.

    Declared as an Enum so that:
    - Pydantic validates the operator value automatically.
    - FastAPI/OpenAPI exposes it as an enum in the schema, so code generators
      create a strongly-typed client.
    """

    EQ = "eq"
    NE = "ne"
    GT = "gt"
    GTE = "gte"
    LT = "lt"
    LTE = "lte"
    LIKE = "like"
    ILIKE = "ilike"
    CONTAINS = "contains"
    ICONTAINS = "icontains"
    IN = "in"
    NOT_IN = "not_in"
    IS_NULL = "is_null"
    IS_NOT_NULL = "is_not_null"


class SearchParams(BaseModel):
    """Normalized search condition shared across repositories."""

    attribute: str
    operator: SearchOperator
    value: Any = None


class OrderDirection(str, Enum):
    """Allowed ordering directions."""

    ASC = "ASC"
    DESC = "DESC"


class OrderParams(BaseModel):
    """Ordering configuration for list endpoints."""

    attribute: str = "uuid"
    direction: OrderDirection = OrderDirection.ASC

    @field_validator("attribute")
    @classmethod
    def validate_attribute(cls, value: str) -> str:
        if not value:
            raise ValueError("Order attribute cannot be empty")
        return value

    @field_validator("direction", mode="before")
    @classmethod
    def normalize_direction(cls, value: str | OrderDirection) -> str | OrderDirection:
        """Allow case-insensitive input and validate direction values."""

        if isinstance(value, OrderDirection):
            return value

        normalized = str(value).upper()
        if normalized not in {OrderDirection.ASC.value, OrderDirection.DESC.value}:
            raise ValueError("Order direction must be ASC or DESC")

        return normalized


class PaginationParams(BaseModel):
    """Pagination configuration received from the client and returned by the API."""

    page: int = 1
    num_items: int = 50
    min_page: Optional[int] = None
    max_page: Optional[int] = None
    total_items: Optional[int] = None

    @field_validator("page", "num_items")
    @classmethod
    def ensure_positive(cls, value: int) -> int:
        if value < 1:
            raise ValueError("Pagination values must be greater than zero")
        return value


class FiltersInterface(BaseModel):
    """Unified filters payload shared by routers, controllers and repositories."""

    search: List[SearchParams] = Field(default_factory=list)
    include_relations: List[str] = Field(default_factory=list)
    pagination: PaginationParams = Field(default_factory=PaginationParams)
    order: OrderParams = Field(default_factory=OrderParams)

    @field_validator("search", mode="after")
    @classmethod
    def normalize_search(cls, value: List[Any]) -> List[SearchParams]:
        normalized: List[SearchParams] = []
        for entry in value or []:
            if isinstance(entry, SearchParams):
                normalized.append(entry)
            elif isinstance(entry, dict):
                try:
                    normalized.append(
                        SearchParams(
                            attribute=entry["attribute"],
                            operator=entry["operator"],
                            value=entry.get("value"),
                        )
                    )
                except KeyError as exc:
                    raise ValueError("Search filters must include attribute and operator") from exc
            else:
                raise ValueError("Unsupported search filter format")
        return normalized

    @classmethod
    def from_raw(cls, raw: Optional[Any]) -> "FiltersInterface":
        """Build a FiltersInterface from any supported raw representation."""

        if raw is None or raw == {}:
            return cls()
        if isinstance(raw, cls):
            return raw
        try:
            return cls.model_validate(raw)
        except ValidationError as exc:
            raise ValueError(str(exc)) from exc


class ListResponse(BaseModel, Generic[T]):
    """Standard list response returned by routers."""

    items: List[T]
    pagination: PaginationParams
    order: OrderParams

