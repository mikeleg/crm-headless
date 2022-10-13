from typing import Protocol, List, Optional
from core.exceptions import AddressIsDoubleAssigned, AddressWithoutParentKey
from core.models.address import Address
from infrastructure.repositories.address import IAddressRepository


class IAddressService(Protocol):
    def all(self, customer_id: int = None, contact_id: int = None) -> List[Address]:
        pass

    def get(self, id: int, customer_id: int = None, contact_id: int = None) -> Optional[Address]:
        pass

    def create(self, Address: Address) -> Address:
        pass

    def update(self, Address: Address) -> Address:
        pass

    def delete(self, id: int) -> None:
        pass


class AddressService:
    def __init__(self, repo: IAddressRepository) -> None:
        self.repo = repo
        super().__init__()

    def all(self, customer_id: int = None, contact_id: int = None) -> List[Address]:

        self._chek_custmer_contact_is_initialized(customer_id, contact_id)

        return self.repo.all(customer_id, contact_id)

    def get(self, id: int, customer_id: int = None, contact_id: int = None) -> Optional[Address]:

        self._chek_custmer_contact_is_initialized(customer_id, contact_id)

        return self.repo.get(id, customer_id, contact_id)

    def create(self, address: Address) -> Address:
        self._chek_custmer_contact_are_both_initialized(address)
        return self.repo.create(address)

    def update(self, address: Address) -> Address:
        self._chek_custmer_contact_are_both_initialized(address)
        return self.repo.update(Address)

    def delete(self, id: int) -> None:
        self.delete(id)

    def _chek_custmer_contact_is_initialized(self, customer_id, contact_id) -> None:
        if customer_id is None and contact_id is None:
            raise AddressWithoutParentKey()

    def _chek_custmer_contact_are_both_initialized(self, address: Address) -> None:
        if address.customer_id is not None and address.contact_id is not None:
            raise AddressIsDoubleAssigned()
