from .models import Lead
from .serializers import LeadSerializer
from rest_framework import mixins,viewsets


class LeadList(mixins.ListModelMixin,viewsets.GenericViewSet):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

class LeadDetail(mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,viewsets.GenericViewSet):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
