from src.application.use_cases.charge_payment_use_case import ChargePayment
from src.config import settings
from src.infrastructure.services.order_service_proxy import OrderServiceProxy


class PaymentDependencies:
    order_service_proxy = OrderServiceProxy(settings)

    @classmethod
    def charge_payment(cls):
        return ChargePayment(cls.order_service_proxy)
