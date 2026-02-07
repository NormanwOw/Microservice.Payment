from enum import Enum


class Currency(str, Enum):
    USD = 'USD'
    EUR = 'EUR'


class CommandType(str, Enum):
    CHARGE_PAYMENT = 'ChargePayment'


class EventType(str, Enum):
    PAYMENT_CHARGED = 'PaymentCharged'
    CHARGE_PAYMENT_FAILED = 'ChargePaymentFailed'


class AggregateType(str, Enum):
    ORDER = 'order'
