from src.application.use_cases.charge_payment_use_case import ChargePayment


class PaymentDependencies:
    @classmethod
    def charge_payment(cls):
        return ChargePayment()
