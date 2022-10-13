from rest_framework import routers
from .views import AddressView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r"address", AddressView, basename="address")
