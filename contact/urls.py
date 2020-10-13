from django.urls import include, path
from contact import viewsets

urlpatterns = [
    path(
        "api/accounts/<int:account_id>/contacts",
        viewsets.ContactCreateList.as_view({"get": "list", "post": "create"}),
        name="account-contact-list",
    ),
    path(
        "api/accounts/<int:account_id>/contact/<int:pk>",
        viewsets.ContactDetail.as_view(
            {"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"}
        ),
        name="account-contact-detail",
    ),
    path(
        "api/leads/<int:lead_id>/contacts",
        viewsets.ContactCreateList.as_view({"get": "list", "post": "create"}),
        name="lead-contact-list",
    ),
    path(
        "api/leads/<int:lead_id>/contacts/<int:pk>",
        viewsets.ContactDetail.as_view(
            {"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"}
        ),
        name="lead-contact-detail",
    ),
]
