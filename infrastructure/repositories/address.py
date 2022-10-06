from typing import Optional, List, Protocol

from core.exceptions import AddressIsDoubleAssigned
from ..models.address import Address
from core.models.address import Address as AddressEntity


class IAddressRepository(Protocol):
    def all(self) -> List[AddressEntity]:
        pass

    def get(self, id: int) -> Optional[AddressEntity]:
        pass

    def create(self, note: AddressEntity) -> AddressEntity:
        pass

    def update(self, note: AddressEntity) -> AddressEntity:
        pass

    def delete(self, id) -> None:
        pass


class AddressRepository:
    def all(self) -> List[AddressEntity]:
        return [self._convert_instance(address) for address in Address.objects.all()]

    def get(self, id: int) -> Optional[AddressEntity]:
        if id is None:
            return None

        return self._convert_instance(Address.objects.filter(id=id).first())

    def create(self, address: AddressEntity) -> AddressEntity:

        if address.customer_id is not None and address.contact_id is not None:
            raise AddressIsDoubleAssigned(
                "Address can't be associated with both customer and contact"
            )

        new_address = Address.objects.create(**address.__dict__)
        new_address.save()

        return self._convert_instance(new_address)

    def update(self, address: AddressEntity) -> AddressEntity:

        if address.customer_id is not None and address.contact_id is not None:
            raise AddressIsDoubleAssigned(
                "Address can't be associated with both customer and contact"
            )

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
        )
