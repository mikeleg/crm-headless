from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
from .models import Note
from .serializers import NoteSerializer


class NoteCreateList(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = NoteSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = None

        if self.kwargs.get("account_id") is not None:
            queryset = Note.objects.filter(account_id__exact=self.kwargs.get("account_id"))
        else:
            return Response("Non è selezionato un'account ", status=status.HTTP_404_NOT_FOUND)
        return queryset


class NoteDetail(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = None

        if self.kwargs.get("account_id") is not None:
            queryset = Note.objects.filter(account_id__exact=self.kwargs.get("account_id"))
        else:
            return Response("Non è selezionato un'account ", status=status.HTTP_404_NOT_FOUND)
        return queryset

    def update(self, request, *args, **kwargs):
        kwargs["partial"] = True
        return super().update(request, *args, **kwargs)