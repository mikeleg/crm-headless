from rest_framework import mixins, viewsets

from .models import Note
from .serializers import NoteSerializer


class NoteCreateList(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = NoteSerializer

    def get_serializer_context(self):
        ctx = super().get_serializer_context()

        ctx.update(
            {"account_id": self.kwargs.get("account_id"), "lead_id": self.kwargs.get("lead_id")}
        )

        return ctx

    def get_queryset(self, *args, **kwargs):
        queryset = Note.objects.all()

        if self.kwargs.get("account_id") is not None:
            queryset = queryset.filter(account_id__exact=self.kwargs.get("account_id"))
        elif self.kwargs.get("lead_id") is not None:
            queryset = queryset.filter(lead_id__exact=self.kwargs.get("lead_id"))

        return queryset


class NoteDetail(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
