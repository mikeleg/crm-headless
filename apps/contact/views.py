from typing import Any

from apps.contact.dto import ContactResponse, UpsertContactRequest
from apps.contact.service import ContactService
from core.api import CrmApiView
from core.models.contact import Contact
from drf_spectacular.openapi import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema
from infrastructure.repositories.contact import ContactRepository
from rest_framework.response import Response


@extend_schema()
class ContactView(CrmApiView):
    def __init__(self, **kwargs: Any) -> None:
        self.service = ContactService(ContactRepository())
        super().__init__(**kwargs)

    @extend_schema(responses=ContactResponse, tags=["contact"], description="Get all contacts")
    def list(self, request):
        contacts = self.service.all()
        return Response(ContactResponse(contacts, many=True).data)

    @extend_schema(
        responses=ContactResponse,
        parameters=[OpenApiParameter("id", OpenApiTypes.INT, OpenApiParameter.PATH)],
        tags=["contact"],
        description="Get contact by id",
    )
    def retrieve(self, request, pk: int):
        contact = self.service.get(id)
        return Response(ContactResponse(contact).data)

    @extend_schema(
        request=UpsertContactRequest,
        responses=ContactResponse,
        parameters=[],
        tags=["contact"],
        description="Create a new contact",
    )
    def create(self, request):
        contact_dto = UpsertContactRequest(data=request.data)

        if not contact_dto.is_valid():
            return Response(contact_dto.errors, status=400)

        contact_domain = Contact(**contact_dto.data)
        contact = self.service.create(contact_domain)

        return Response(ContactResponse(contact).data)

    @extend_schema(
        request=UpsertContactRequest,
        responses=ContactResponse,
        parameters=[],
        tags=["contact"],
        description="Update a contact",
    )
    def update(self, request, pk: int):
        contact_dto = UpsertContactRequest(data=request.data)

        if not contact_dto.is_valid():
            return Response(contact_dto.errors, status=400)

        contact_domain = Contact(**contact_dto.data)
        contact_domain.id = pk
        contact = self.service.update(contact_domain)

        return Response(ContactResponse(contact).data)

    @extend_schema(
        parameters=[OpenApiParameter("id", OpenApiTypes.INT, OpenApiParameter.PATH)],
        tags=["contact"],
        description="Delete a contact",
    )
    def destroy(self, request, pk: int):

        self.service.delete(pk)

        return Response()
