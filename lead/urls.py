from django.urls import include, path
from rest_framework import routers
from lead import viewsets
from contact import viewsets as contact_viewsets
from note import viewsets as note_viewsets
import note

router = routers.DefaultRouter(trailing_slash=False)
router.register(r"leads", viewsets.LeadDetail, "lead-detail")
router.register(r"leads", viewsets.LeadCreateList, "lead-list")

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("api/", include(router.urls)),
    path(
        "api/leads/<int:lead_id>/contacts",
        contact_viewsets.ContactCreateList.as_view({"get": "list", "post": "create"}),
        name="lead-contact-list",
    ),
    path(
        "api/leads/<int:lead_id>/contacts/<int:pk>",
        contact_viewsets.ContactDetail.as_view(
            {"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"}
        ),
        name="lead-contact-detail",
    ),
    path(
        "api/leads/<int:lead_id>/notes",
        note_viewsets.NoteCreateList.as_view({"get": "list", "post": "create"}),
        name="lead-note-list",
    ),
    path(
        "api/leads/<int:lead_id>/notes/<int:pk>",
        note_viewsets.NoteDetail.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
        name="lead-note-detail",
    ),
]
