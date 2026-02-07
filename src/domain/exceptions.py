class DomainException(Exception):
    def __init__(self, detail: str):
        self.detail = detail


class CustomerNotFoundException(DomainException): ...


class NotEnoughFundsException(DomainException): ...
