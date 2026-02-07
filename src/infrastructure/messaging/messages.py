from datetime import datetime
from decimal import Decimal
from uuid import UUID, uuid4

from pydantic import Field

from src.domain.base import PydanticBase
from src.domain.enums import AggregateType, CommandType, Currency, EventType


class Message(PydanticBase):
    message_id: UUID = Field(default_factory=uuid4)
    producer: str
    sent_at: datetime | None = None


class ExternalReference(PydanticBase):
    id: UUID
    type: AggregateType
    version: int


class EventMessage(Message):
    action: EventType
    external_reference: ExternalReference


class CommandMessage(Message):
    action: CommandType
    external_reference: ExternalReference


class ChargePaymentPayload(PydanticBase):
    user_id: UUID
    amount: Decimal
    currency: Currency


class ChargePaymentMessage(CommandMessage):
    payload: ChargePaymentPayload
