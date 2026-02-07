from src.domain.base import PydanticBase


class PaymentData(PydanticBase):
    customer_id: str
    customer_email: str
    order_id: str
    order_amount: int
