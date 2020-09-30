from django.urls import include, path
from rest_framework import routers
from account import viewsets

router = routers.DefaultRouter()
router.register(r"account", viewsets.AccountDetail, "account-detail")
router.register(r"accounts", viewsets.AccountCreateList, "account-list")

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("", include(router.urls)),
]
