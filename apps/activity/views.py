from typing import Any

from apps import activity
from apps.activity.dto import ActivityResponse, UpsertActivityRequest
from apps.activity.service import ActivityService
from core.api import CrmApiView
from drf_spectacular.openapi import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema
from infrastructure.repositories.activity import ActivityRepository
from rest_framework.response import Response


class ActivityView(CrmApiView):
    def __init__(self, **kwargs):
        self.service = ActivityService(ActivityRepository())
        super().__init__(**kwargs)

    @extend_schema(responses=ActivityResponse, tags=["activity"])
    def list(self, request):
        activities = self.service.all()
        return Response(ActivityResponse(activities, many=True).data)

    @extend_schema(
        responses=ActivityResponse,
        tags=["activity"],
        parameters=[OpenApiParameter("id", OpenApiTypes.INT, OpenApiParameter.PATH)],
    )
    def retrieve(self, request, pk: int):
        activity = self.service.get(pk)
        return Response(ActivityResponse(activity).data)

    @extend_schema(request=UpsertActivityRequest, responses=ActivityResponse, tags=["activity"])
    def create(self, request):
        activity_dto = UpsertActivityRequest(data=request.data)

        if not activity_dto.is_valid():
            return Response(activity_dto.errors, status=400)

        activity_domain = activity.Activity(**activity_dto.data)
        new_activity = self.service.create(activity_domain)

        return Response(ActivityResponse(new_activity).data)

    @extend_schema(
        request=UpsertActivityRequest,
        responses=ActivityResponse,
        tags=["activity"],
        parameters=[OpenApiParameter("id", OpenApiTypes.INT, OpenApiParameter.PATH)],
    )
    def update(self, request, pk: int):
        activity_dto = UpsertActivityRequest(data=request.data)

        if not activity_dto.is_valid():
            return Response(activity_dto.errors, status=400)

        activity_domain = activity.Activity(**activity_dto.data)
        activity_domain.id = pk
        updated_activity = self.service.update(activity_domain)

        return Response(ActivityResponse(updated_activity).data)

    @extend_schema(
        tags=["activity"],
        parameters=[OpenApiParameter("id", OpenApiTypes.INT, OpenApiParameter.PATH)],
    )
    def destroy(self, request, pk: int):
        self.service.delete(pk)
        return Response()
