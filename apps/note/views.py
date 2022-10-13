from typing import Any

from apps.note.dto import NoteResponse, UpsertNoteRequest
from apps.note.service import NoteService
from core.api import CrmApiView
from core.models.note import Note
from drf_spectacular.openapi import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema
from infrastructure.repositories.note import NoteRepository
from rest_framework.response import Response


@extend_schema()
class NoteView(CrmApiView):
    def __init__(self, **kwargs: Any) -> None:
        self.service = NoteService(NoteRepository())
        super().__init__(**kwargs)

    @extend_schema(responses=NoteResponse, tags=["note"], description="Get all note")
    def list(self, request):
        notes = self.service.all()
        return Response(NoteResponse(notes, many=True).data)

    @extend_schema(
        responses=NoteResponse,
        parameters=[OpenApiParameter("id", OpenApiTypes.INT, OpenApiParameter.PATH)],
        tags=["note"],
        description="Get note by id",
    )
    def retrieve(self, request, pk: int):
        note = self.service.get(pk)
        return Response(NoteResponse(note, many=True).data)

    @extend_schema(
        request=UpsertNoteRequest,
        responses=NoteResponse,
        tags=["note"],
        description="Create note",
    )
    def create(self, request: UpsertNoteRequest):
        note_dto = UpsertNoteRequest(data=request.data)

        if not note_dto.is_valid():
            return Response(note_dto.errors, status=400)

        node_domain = Note(**note_dto.data)
        note = self.service.create(node_domain)

        return Response(NoteResponse(note).data)

    @extend_schema(
        request=UpsertNoteRequest,
        responses=NoteResponse,
        parameters=[OpenApiParameter("id", OpenApiTypes.INT, OpenApiParameter.PATH)],
        tags=["note"],
        description="Update note",
    )
    def update(self, request: UpsertNoteRequest, pk: int):
        note_dto = UpsertNoteRequest(data=request.data)

        if not note_dto.is_valid():
            return Response(note_dto.errors, status=400)

        node_domain = Note(**note_dto.data)
        node_domain.id = pk
        updated_note = self.service.update(node_domain)

        return Response(NoteResponse(updated_note).data)

    @extend_schema(
        responses=Any,
        parameters=[OpenApiParameter("id", OpenApiTypes.INT, OpenApiParameter.PATH)],
        tags=["note"],
        description="Delete note",
    )
    def destroy(self, request: Any, pk: int):

        self.service.delete(pk)

        return Response()
