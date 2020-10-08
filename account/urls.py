from django.urls import include, path
from rest_framework import routers
from account import viewsets
from contact import viewsets as contact_viewsets
from note import viewsets as note_viewsets

router = routers.DefaultRouter(trailing_slash=False)
router.register(r"accounts", viewsets.AccountDetail, "account-detail")
router.register(r"accounts", viewsets.AccountCreateList, "account-list")

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("api/", include(router.urls)),
    path(
        "api/accounts/<int:account_id>/contacts",
        contact_viewsets.ContactCreateList.as_view({"get": "list", "post": "create"}),
        name="account-contact-list",
    ),
    path(
        "api/accounts/<int:account_id>/contact/<int:pk>",
        contact_viewsets.ContactDetail.as_view(
            {"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"}
        ),
        name="account-contact-detail",
    ),
    path(
        "api/accounts/<int:account_id>/notes",
        note_viewsets.NoteCreateList.as_view({"get": "list", "post": "create"}),
        name="account-note-list",
    ),
    path(
        "api/accounts/<int:account_id>/notes/<int:pk>",
        note_viewsets.NoteDetail.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
        name="account-note-detail",
    ),
]
