from src.config import Settings
from src.domain.enums import EventType
from src.infrastructure.messaging.messages import ExternalReference
from src.infrastructure.models import OutboxModel
from src.infrastructure.services.interfaces import IOrderService
from src.infrastructure.uow.interfaces import IUnitOfWork


class OrderServiceProxy(IOrderService):
    def __init__(self, settings: Settings):
        self.topic = settings.SAGA_EVENTS_TOPIC
        self.producer = 'payment-service'

    async def payment_charged(self, uow: IUnitOfWork, external_reference: ExternalReference):
        for_outbox = OutboxModel(
            action=EventType.PAYMENT_CHARGED,
            topic=self.topic,
            payload={},
            external_reference=external_reference.to_dict(),
            producer=self.producer,
        )
        await uow.outbox.add(for_outbox)

    async def charge_payment_failed(
        self, uow: IUnitOfWork, error_message: str, external_reference: ExternalReference
    ):
        for_outbox = OutboxModel(
            action=EventType.CHARGE_PAYMENT_FAILED,
            topic=self.topic,
            payload={'error_message': error_message},
            external_reference=external_reference.to_dict(),
            producer=self.producer,
        )
        await uow.outbox.add(for_outbox)
