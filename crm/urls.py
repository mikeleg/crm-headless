from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

from apps.customer.router import router as router_customer
from apps.contact.router import router as router_contact
from apps.note.router import router as router_note
from apps.activity.router import router as router_activity
from apps.address.router import router as router_address


urlpatterns = [
    path("admin/", admin.site.urls),
]

urlpatterns = [
    path("api/", include(router_customer.urls)),
    path("api/", include(router_contact.urls)),
    path("api/", include(router_note.urls)),
    path("api/", include(router_activity.urls)),
    path("api/customers/<int:customer_id>/", include(router_address.urls)),
    path("api/contacts/<int:contact_id>/", include(router_address.urls)),
]

urlpatterns += [
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/doc/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
]
