from typing import Any

from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base


BaseSchema: Any = declarative_base()


class TenantSchema:
    """
    ModelSchema base with tenant_id field for multi-tenant support
    """

    @staticmethod
    def tenant_column() -> Column:
        return Column("tenant_id", String(255), nullable=True)