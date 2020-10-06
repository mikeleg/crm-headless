from rest_framework import mixins, viewsets

from .models import Contact
from .serializers import ContactSerializer


class ContactCreateList(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = ContactSerializer

    def get_serializer_context(self):
        ctx = super().get_serializer_context()

        ctx.update(
            {"account_id": self.kwargs.get("account_id"), "lead_id": self.kwargs.get("lead_id")}
        )

        return ctx

    def get_queryset(self, *args, **kwargs):
        queryset = Contact.objects.all()

        if self.kwargs.get("account_id") is not None:
            queryset = queryset.filter(account_id__exact=self.kwargs.get("account_id"))
        elif self.kwargs.get("lead_id") is not None:
            queryset = queryset.filter(lead_id__exact=self.kwargs.get("lead_id"))

        return queryset


class ContactDetail(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
