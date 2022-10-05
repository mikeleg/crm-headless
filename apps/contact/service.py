import re
from typing import Protocol, List, Optional
from core.models.contact import Contact
from infrastructure.repositories.contact import IContactRepository


class IContactService(Protocol):
    def all(self) -> List[Contact]:
        pass

    def get(self, id: int) -> Optional[Contact]:
        pass

    def create(self, contact: Contact) -> Contact:
        pass

    def update(self, contact: Contact) -> Contact:
        pass

    def delete(self, id: int) -> None:
        pass


class ContactService:
    def __init__(self, repo: IContactRepository) -> None:
        self.repo = repo

    def all(self) -> List[Contact]:
        return self.repo.all()

    def get(self, id: int) -> Optional[Contact]:
        return self.repo.get(id)

    def create(self, contact: Contact) -> Contact:
        return self.repo.create(contact)

    def update(self, contact: Contact) -> Contact:
        return self.repo.update(contact)

    def delete(self, id: int) -> None:
        self.repo.delete(id)
