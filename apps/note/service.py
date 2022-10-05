import re
from typing import Protocol, List, Optional
from core.models.note import Note
from infrastructure.repositories.note import INoteRepository


class INoteService(Protocol):
    def all(self) -> List[Note]:
        pass

    def get(self, id: int) -> Optional[Note]:
        pass

    def create(self, note: Note) -> Note:
        pass

    def update(self, note: Note) -> Note:
        pass

    def delete(self, id: int) -> None:
        pass


class NoteService:
    def __init__(self, repo: INoteRepository) -> None:
        self.repo = repo
        super().__init__()

    def all(self) -> List[Note]:
        return self.repo.all()

    def get(self, id: int) -> Optional[Note]:
        return self.repo.get(id)

    def create(self, note: Note) -> Note:
        return self.repo.create(note)

    def update(self, note: Note) -> Note:
        note.id = id
        return self.repo.update(note)

    def delete(self, id: int) -> None:
        self.delete(id)
