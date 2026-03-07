from sqlalchemy.ext.asyncio import AsyncSession

from src.application.ports.repositories import ICustomerRepository
from src.infrastructure.models import CustomerModel
from src.infrastructure.repositories.base_repository import SQLAlchemyRepository


class CustomerRepository(SQLAlchemyRepository, ICustomerRepository):
    def __init__(self, session: AsyncSession):
        self.__session = session
        super().__init__(session, CustomerModel)
