from rest_framework import mixins, viewsets

from .models import Contact
from .serializers import ContactSerializer


class ContactCreateList(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class ContactDetail(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
