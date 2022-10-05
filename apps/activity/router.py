from rest_framework import routers
from .views import ActivityView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r"activity", ActivityView, basename="activities")
