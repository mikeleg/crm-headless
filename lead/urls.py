from django.urls import include, path
from rest_framework import routers
from lead import viewsets

router = routers.DefaultRouter()
router.register(r'lead', viewsets.LeadDetail,'lead-detail')
router.register(r'leads', viewsets.LeadList,'lead-list')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]