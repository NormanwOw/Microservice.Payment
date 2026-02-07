from src.application.disp_depends import DispDepends
from src.application.dispatcher import dispatcher
from src.application.use_cases.charge_payment_use_case import ChargePayment
from src.domain.dto import PaymentData
from src.domain.enums import CommandType
from src.domain.exceptions import DomainException
from src.infrastructure.logger.impl import logger
from src.infrastructure.messaging.messages import ChargePaymentMessage
from src.infrastructure.uow.interfaces import IUnitOfWork
from src.presentation.dependencies import PaymentDependencies


@dispatcher.register(CommandType.CHARGE_PAYMENT)
async def charge_payment_handler(
    uow: IUnitOfWork,
    message: dict,
    charge_payment: ChargePayment = DispDepends(PaymentDependencies.charge_payment),
):
    try:
        msg = ChargePaymentMessage(**message)
        payment_data: PaymentData = await charge_payment(uow, msg)
        logger.info(
            f'Successfully charged payment from customer {payment_data.customer_id} | '
            f'order id: {payment_data.order.id}, '
            f'amount {payment_data.order.amount}{payment_data.order.currency.value}, '
            f'command message id: {msg.message_id}'
        )
    except DomainException as ex:
        logger.info(ex.detail)
