from django.urls import include, path
from note import viewsets

urlpatterns = [
    path(
        "api/leads/<int:lead_id>/notes",
        viewsets.NoteCreateList.as_view({"get": "list", "post": "create"}),
        name="lead-note-list",
    ),
    path(
        "api/leads/<int:lead_id>/notes/<int:pk>",
        viewsets.NoteDetail.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}),
        name="lead-note-detail",
    ),
    path(
        "api/accounts/<int:accounts_id>/notes",
        viewsets.NoteCreateList.as_view({"get": "list", "post": "create"}),
        name="lead-note-list",
    ),
    path(
        "api/accounts/<int:accounts_id>/notes/<int:pk>",
        viewsets.NoteDetail.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}),
        name="lead-note-detail",
    ),
]
