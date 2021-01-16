from django.urls import include, path
from rest_framework import routers
from .viewsets import ContactCreateList

router = routers.DefaultRouter(trailing_slash=False)
# router.register(r"account", viewsets.AccountDetail, "account")
router.register(r"contact", ContactCreateList, "contact")

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("account/<int:account_id>/", include(router.urls)),
]
