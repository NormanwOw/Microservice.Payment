from uuid import UUID

from src.domain.base import PydanticBase
from src.domain.entities import Order


class PaymentData(PydanticBase):
    customer_id: UUID
    order: Order
