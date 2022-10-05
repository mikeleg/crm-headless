from typing import Optional, List, Protocol
from ..models.note import Note
from core.models.note import Note as NoteEntity


class INoteRepository(Protocol):
    def all(self) -> List[NoteEntity]:
        pass

    def get(self, id: int) -> Optional[NoteEntity]:
        pass

    def create(self, note: NoteEntity) -> NoteEntity:
        pass

    def update(self, note: NoteEntity) -> NoteEntity:
        pass

    def delete(self, id) -> None:
        pass


class NoteRepository:
    def all(self) -> List[NoteEntity]:
        return [self._convert_instance(note) for note in Note.objects.all()]

    def get(self, id: int) -> Optional[NoteEntity]:
        if id is None:
            return None

        return self._convert_instance(Note.objects.filter(id=id).first())

    def create(self, note: NoteEntity) -> NoteEntity:
        new_note = Note.objects.create(**note.__dict__)
        new_note.save()

        return self._convert_instance(new_note)

    def update(self, note: NoteEntity) -> NoteEntity:

        Note.objects.filter(id=note.id).update(**note.__dict__)
        updated_note = Note.objects.filter(id=note.id).first()

        return self._convert_instance(updated_note)

    def delete(self, id) -> None:
        Note.objects.filter(id=id).delete()

    @staticmethod
    def _convert_instance(instance: Note) -> NoteEntity:
        return NoteEntity(
            id=instance.id,
            description=instance.description,
            customer_id=instance.customer_id,
        )
