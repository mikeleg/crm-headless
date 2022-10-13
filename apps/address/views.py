from typing import Any

from core.api import CrmApiView
from core.models.address import Address
from drf_spectacular.openapi import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema
from infrastructure.repositories.address import AddressRepository
from rest_framework.response import Response

from .dto import AddressResponse, UpsertAddressRequest
from .service import AddressService


class AddressView(CrmApiView):
    def __init__(self, **kwargs: Any) -> None:
        self.service = AddressService(AddressRepository())
        super().__init__(**kwargs)

    @extend_schema(
        responses=AddressResponse,
        parameters=[],
        tags=["address"],
        description="Get all addresses",
    )
    def list(self, request, **kwargs):
        customer_pk, contact_pk = self._get_parent_key(kwargs)
        addresses = self.service.all(customer_pk, contact_pk)
        return Response(AddressResponse(addresses, many=True).data)

    @extend_schema(
        responses=AddressResponse,
        parameters=[
            OpenApiParameter("id", OpenApiTypes.INT, OpenApiParameter.PATH),
        ],
        tags=["address"],
        description="Get address",
    )
    def retrieve(self, request, pk: int, **kwargs):
        customer_pk, contact_pk = self._get_parent_key(kwargs)
        addresses = self.service.get(pk, customer_pk, contact_pk)
        return Response(AddressResponse(addresses, many=True).data)

    @extend_schema(
        request=UpsertAddressRequest,
        responses=AddressResponse,
        parameters=[],
        tags=["address"],
        description="Create address",
    )
    def create(self, request: UpsertAddressRequest, **kwargs):
        customer_pk, contact_pk = self._get_parent_key(kwargs)
        address_dto = UpsertAddressRequest(data=request.data)

        if not address_dto.is_valid():
            return Response(address_dto.errors, status=400)

        address_domain = Address(**address_dto.data)
        address_domain.contact_id = contact_pk
        address_domain.customer_id = customer_pk
        address = self.service.create(address_domain)

        return Response(AddressResponse(address).data)

    @extend_schema(
        request=UpsertAddressRequest,
        responses=AddressResponse,
        parameters=[
            OpenApiParameter("id", OpenApiTypes.INT, OpenApiParameter.PATH),
        ],
        tags=["address"],
        description="Update address",
    )
    def update(self, request: UpsertAddressRequest, pk: int, **kwargs):
        customer_pk, contact_pk = self._get_parent_key(kwargs)
        address_dto = UpsertAddressRequest(data=request.data)

        if not address_dto.is_valid():
            return Response(address_dto.errors, status=400)

        address_domain = Address(**address_dto.data)
        address_domain.concat_id = contact_pk
        address_domain.customer_id = customer_pk
        address_domain.id = pk
        updated_address = self.service.update(address_domain)

        return Response(AddressResponse(updated_address).data)

    @extend_schema(
        responses=Any,
        parameters=[
            OpenApiParameter("id", OpenApiTypes.INT, OpenApiParameter.PATH),
        ],
        tags=["address"],
        description="Delete address",
    )
    def destroy(self, request: Any, pk: int):

        self.service.delete(pk)

        return Response()

    def _get_parent_key(self, kwargs) -> tuple[int, int]:
        customer_pk = kwargs.get("customer_id")
        contact_pk = kwargs.get("contact_id")
        return customer_pk, contact_pk
