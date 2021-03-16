from django.http import response
from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
from .models import Contact
from .serializers import ContactSerializer


class ContactCreateList(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = ContactSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = None

        if self.kwargs.get("account_id") is not None:
            queryset = Contact.objects.filter(account_id=self.kwargs.get("account_id"))
        else:
            return Response("Non è selezionato un'account ", status=status.HTTP_404_NOT_FOUND)
        return queryset

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class ContactDetail(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = None

        if self.kwargs.get("account_id") is not None:
            queryset = Contact.objects.filter(account_id__exact=self.kwargs.get("account_id"))
        else:
            return Response("Non è selezionato un'account ", status=status.HTTP_404_NOT_FOUND)
        return queryset

    def update(self, request, *args, **kwargs):
        kwargs["partial"] = True
        return super().update(request, *args, **kwargs)
