from decimal import Decimal

from src.application.ports.services import IOrderService
from src.application.ports.uow import IUnitOfWork
from src.domain.dto import PaymentData
from src.domain.entities import Order
from src.domain.exceptions import NotEnoughFundsException
from src.infrastructure.messaging.messages import ChargePaymentMessage
from src.infrastructure.models import CustomerModel


class ChargePayment:
    def __init__(self, order_service_proxy: IOrderService):
        self.order_service_proxy = order_service_proxy

    async def __call__(self, uow: IUnitOfWork, message: ChargePaymentMessage) -> PaymentData:
        customer: CustomerModel = await uow.customers.find_one(
            CustomerModel.id, message.payload.user_id, with_for_update=True
        )
        if not customer:
            customer = CustomerModel(
                id=message.payload.user_id,
                balance=Decimal('10000.00'),
            )
            await uow.customers.add(customer)
        if customer.balance < message.payload.amount:
            error_message = f'Customer with id {message.payload.user_id} not enough funds'
            await self.order_service_proxy.charge_payment_failed(
                uow=uow, error_message=error_message, external_reference=message.external_reference
            )
            raise NotEnoughFundsException(detail=error_message)

        customer.balance -= message.payload.amount
        await self.order_service_proxy.payment_charged(uow, message.external_reference)
        return PaymentData(
            customer_id=customer.id,
            order=Order(
                id=message.external_reference.id,
                amount=message.payload.amount,
                currency=message.payload.currency,
            ),
        )
