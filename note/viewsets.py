from rest_framework import mixins, viewsets

from .models import Note
from .serializers import NoteSerializer


class NoteCreateList(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = NoteSerializer


class NoteDetail(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
