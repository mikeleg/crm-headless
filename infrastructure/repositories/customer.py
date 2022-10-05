from typing import Optional, List, Protocol
from ..models.customer import Customer
from core.models.customer import Customer as CustomerEntity


class ICustomerRepository(Protocol):
    def all(self) -> List[CustomerEntity]:
        pass

    def get(self, id: int) -> Optional[CustomerEntity]:
        pass

    def create(self, note: CustomerEntity) -> CustomerEntity:
        pass

    def update(self, note: CustomerEntity) -> CustomerEntity:
        pass

    def delete(self, id) -> None:
        pass


class CustomerRepository:
    def all(self) -> List[CustomerEntity]:
        return [self._convert_instance(customer) for customer in Customer.objects.all()]

    def get(self, id: int) -> Optional[CustomerEntity]:
        if id is None:
            return None

        customer = Customer.objects.filter(id=id).first()

        return self._convert_instance(customer)

    def create(self, customer: CustomerEntity) -> CustomerEntity:
        new_customer = Customer(**customer.__dict__)
        new_customer.save()

        return self._convert_instance(new_customer)

    def update(self, customer: CustomerEntity) -> CustomerEntity:
        Customer.objects.filter(id=customer.id).update(**customer.__dict__)

        updated_customer = Customer.objects.filter(id=customer.id).first()

        return self._convert_instance(updated_customer)

    def delete(self, id) -> None:
        Customer.objects.filter(id=id).delete()

    @staticmethod
    def _convert_instance(instance: Customer) -> CustomerEntity:
        return CustomerEntity(
            id=instance.id,
            nickname=instance.nickname,
            legalname=instance.legalname,
            phone=instance.phone,
            email=instance.email,
            address=instance.address,
            city=instance.city,
            country=instance.country,
            province=instance.province,
            zipcode=instance.zipcode,
            geo=instance.geo,
            pec=instance.pec,
            sdi=instance.sdi,
            vat=instance.vat,
            type=instance.type,
        )
