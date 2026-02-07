from src.infrastructure.messaging.messages import ChargePaymentMessage
from src.infrastructure.uow.interfaces import IUnitOfWork


class ChargePayment:
    async def __call__(self, uow: IUnitOfWork, message: ChargePaymentMessage):
        async with uow:
            pass
