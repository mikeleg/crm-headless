from rest_framework import mixins, viewsets

from .models import Lead
from .serializers import LeadSerializer


class LeadList(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer


class LeadDetail(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
