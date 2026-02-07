from decimal import Decimal
from uuid import UUID

from src.domain.base import PydanticBase
from src.domain.enums import Currency


class Order(PydanticBase):
    id: UUID
    amount: Decimal
    currency: Currency
