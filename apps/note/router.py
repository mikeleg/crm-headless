from rest_framework import routers
from .views import NoteView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r"note", NoteView, basename="note")
