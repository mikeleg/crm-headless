from os import name
from account.models import Account
from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Lead
from .serializers import LeadSerializer


class LeadCreateList(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer


class LeadDetail(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

    @action(detail=True, methods=["POST"], name="Convert lead into account")
    def convert_to_account(self, request, pk=None):
        pass  # put method in a queue
