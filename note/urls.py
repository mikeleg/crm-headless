from django.urls import include, path
from rest_framework import routers
from .viewsets import NoteCreateList,NoteDetail

router = routers.DefaultRouter(trailing_slash=False)
router.register(r"note", NoteCreateList, "note")
router.register(r"note", NoteDetail, "note")

urlpatterns = [
    path("account/<int:account_id>/", include(router.urls)),
]
