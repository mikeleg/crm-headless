from re import S
from typing import Any
from apps.customer.dto import UpsertCustomerRequest, CustomerResponse
from apps.customer.service import CustomerService
from core.api import CrmApiView
from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.openapi import OpenApiTypes
from rest_framework.response import Response

from core.models.customer import Customer

from infrastructure.repositories.customer import CustomerRepository


class CustomerView(CrmApiView):
    def __init__(self, **kwargs: Any) -> None:
        self.service = CustomerService(CustomerRepository())
        super().__init__(**kwargs)

    @extend_schema(responses=CustomerResponse, tags=["customer"], description="Get all customers")
    def list(self, request):
        customers = self.service.all()
        return Response(CustomerResponse(customers, many=True).data)

    @extend_schema(
        responses=CustomerResponse,
        parameters=[OpenApiParameter("id", OpenApiTypes.INT, OpenApiParameter.PATH)],
        tags=["customer"],
        description="Get customer by id",
    )
    def retrieve(self, pk: int, request):
        customer = self.service.get(pk)
        return Response(CustomerResponse(customer).data)

    @extend_schema(
        request=UpsertCustomerRequest,
        responses=CustomerResponse,
        tags=["customer"],
        description="Create a new customer",
    )
    def create(self, request):
        customer_dto = UpsertCustomerRequest(data=request.data)

        if not customer_dto.is_valid():
            return Response(customer_dto.errors, status=400)

        customer_domain = Customer(**customer_dto.data)

        customer = self.service.create(customer_domain)

        return Response(CustomerResponse(customer).data)

    @extend_schema(
        request=UpsertCustomerRequest,
        responses=CustomerResponse,
        parameters=[OpenApiParameter("id", OpenApiTypes.INT, OpenApiParameter.PATH)],
        tags=["customer"],
        description="Update a customer",
    )
    def update(self, request, pk: int):

        customer_dto = UpsertCustomerRequest(data=request.data)

        if not customer_dto.is_valid():
            return Response(customer_dto.errors, status=400)

        customer_dto.id = pk
        customer = self.service.update(customer_dto)

        return Response(CustomerResponse(customer).data)

    @extend_schema(
        responses=Any,
        tags=["customer"],
        description="Delete a customer",
        parameters=[OpenApiParameter("id", OpenApiTypes.INT, OpenApiParameter.PATH)],
    )
    def destroy(self, request, pk: int):
        self.service.delete(pk)
        return Response()
