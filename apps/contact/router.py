from rest_framework import routers
from .views import ContactView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r"contact", ContactView, basename="contacts")
