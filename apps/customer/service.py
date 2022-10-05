import re
from typing import Protocol, List, Optional
from core.models.customer import Customer
from infrastructure.repositories.customer import ICustomerRepository


class ICustomerService(Protocol):
    def all(self) -> List[Customer]:
        pass

    def get(self, id: int) -> Optional[Customer]:
        pass

    def create(self, customer: Customer) -> Customer:
        pass

    def update(self, customer: Customer) -> Customer:
        pass

    def delete(self, id: int) -> None:
        pass


class CustomerService:
    def __init__(self, repo: ICustomerRepository) -> None:
        self.repo = repo

    def all(self) -> List[Customer]:
        return self.repo.all()

    def get(self, id: int) -> Optional[Customer]:
        return self.repo.get(id)

    def create(self, customer: Customer) -> Customer:
        return self.repo.create(customer)

    def update(self, customer: Customer) -> Customer:
        return self.repo.update(customer)

    def delete(self, id: int) -> None:
        self.repo.delete(id)
