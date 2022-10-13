from typing import Optional, List, Protocol
from ..models.contact import Contact
from core.models.contact import Contact as ContactEntity


class IContactRepository(Protocol):
    def all(self) -> List[ContactEntity]:
        pass

    def get(self, id: int) -> Optional[ContactEntity]:
        pass

    def create(self, note: ContactEntity) -> ContactEntity:
        pass

    def update(self, note: ContactEntity) -> ContactEntity:
        pass

    def delete(self, id) -> None:
        pass


class ContactRepository:
    def all(self) -> List[ContactEntity]:
        return [self._convert_instance(contact) for contact in Contact.objects.all()]

    def get(self, id: int) -> Optional[ContactEntity]:
        if id is None:
            return None

        return self._convert_instance(Contact.objects.filter(id=id).first())

    def create(self, note: ContactEntity) -> ContactEntity:
        new_contact = Contact.objects.create(**note.__dict__)
        new_contact.save()

        return self._convert_instance(new_contact)

    def update(self, note: ContactEntity) -> ContactEntity:
        updated_contact = Contact.objects.filter(id=note.id).first()
        updated_contact.update(**note.__dict__)

        return self._convert_instance(updated_contact)

    def delete(self, id) -> None:
        Contact.objects.filter(id=id).delete()

    @staticmethod
    def _convert_instance(instance: Contact) -> ContactEntity:
        return ContactEntity(
            id=instance.id,
            nickname=instance.nickname,
            customer_id=instance.customer_id,
            name=instance.name,
            phone=instance.phone,
            surname=instance.surname,
            email=instance.email,
            job_title=instance.job_title,
        )
