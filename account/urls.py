from django.urls import include, path
from rest_framework import routers
from account import viewsets

router = routers.DefaultRouter(trailing_slash=False)
router.register(r"account", viewsets.AccountDetail, "account")
router.register(r"account", viewsets.AccountCreateList, "account")

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("", include(router.urls)),
]
