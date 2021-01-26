from django.urls import include, path
from rest_framework import routers
from .viewsets import ContactCreateList, ContactDetail

router = routers.DefaultRouter(trailing_slash=False)
router.register(r"contact", ContactDetail, "contact")
router.register(r"contact", ContactCreateList, "contact")

urlpatterns = [
    path("account/<int:account_id>/", include(router.urls)),
]
