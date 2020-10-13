from django.urls import include, path
from rest_framework import routers
from account import viewsets
from note import viewsets as note_viewsets

router = routers.DefaultRouter(trailing_slash=False)
router.register(r"accounts", viewsets.AccountDetail, "account-detail")
router.register(r"accounts", viewsets.AccountCreateList, "account-list")

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("api/", include(router.urls)),
]
