from rest_framework import routers
from .views import CustomerView

router = routers.DefaultRouter(trailing_slash=False)
router.register(
    r"customer",
    CustomerView,
    basename="customer",
)
