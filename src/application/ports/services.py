from abc import ABC, abstractmethod

from src.application.ports.uow import IUnitOfWork
from src.infrastructure.messaging.messages import ExternalReference


class IOrderService(ABC):
    @abstractmethod
    async def payment_charged(self, uow: IUnitOfWork, external_reference: ExternalReference):
        raise NotImplementedError

    @abstractmethod
    async def charge_payment_failed(
        self, uow: IUnitOfWork, error_message: str, external_reference: ExternalReference
    ):
        raise NotImplementedError
