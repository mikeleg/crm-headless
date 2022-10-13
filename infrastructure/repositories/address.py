from typing import Optional, List, Protocol

from core.exceptions import AddressIsDoubleAssigned, AddressWithoutParentKey
from ..models.address import Address
from core.models.address import Address as AddressEntity


class IAddressRepository(Protocol):
    def all(self, customer_id: int = None, contact_id: int = None) -> List[AddressEntity]:
        pass

    def get(
        self, id: int, customer_id: int = None, contact_id: int = None
    ) -> Optional[AddressEntity]:
        pass

    def create(self, note: AddressEntity) -> AddressEntity:
        pass

    def update(self, note: AddressEntity) -> AddressEntity:
        pass

    def delete(self, id) -> None:
        pass


class AddressRepository:
    def all(self, customer_id: int = None, contact_id: int = None) -> List[AddressEntity]:
        addresses = None

        if customer_id is not None:
            addresses = Address.objects.filter(customer_id=customer_id)
        elif contact_id is not None:
            addresses = Address.objects.filter(contact_id=contact_id)

        if addresses is None:
            return []

        return [self._convert_instance(address) for address in addresses]

    def get(
        self, id: int, customer_id: int = None, contact_id: int = None
    ) -> Optional[AddressEntity]:

        address = None

        if customer_id is not None:
            address = Address.objects.filter(customer_id=customer_id).filter(id=id).first()
        elif contact_id is not None:
            address = Address.objects.filter(contact_id=contact_id).filter(id=id).first()

        if address is None:
            return None

        return self._convert_instance(address)

    def create(self, address: AddressEntity) -> AddressEntity:

        new_address = Address.objects.create(**address.__dict__)
        new_address.save()

        return self._convert_instance(new_address)

    def update(self, address: AddressEntity) -> AddressEntity:

        address.objects.filter(id=address.id).update(**address.__dict__)
        address_updated = Address.objects.filter(id=address.id).first()

        return self._convert_instance(address_updated)

    def delete(self, id) -> None:
        Address.objects.filter(id=id).delete()

    @staticmethod
    def _convert_instance(instance: Address) -> AddressEntity:
        return AddressEntity(
            id=instance.id,
            nickname=instance.nickname,
            city=instance.city,
            country=instance.country,
            street=instance.street,
            zip_code=instance.zip_code,
            number=instance.number,
            customer_id=instance.customer_id,
            contact_id=instance.contact_id,
            type=instance.type,
        )
