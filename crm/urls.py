from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from apps.customer.router import router as router_customer
from apps.contact.router import router as router_contact
from apps.note.router import router as router_note
from apps.activity.router import router as router_activity


urlpatterns = [
    path("admin/", admin.site.urls),
]

urlpatterns = [
    path("api/", include(router_customer.urls)),
    path("api/", include(router_contact.urls)),
    path("api/", include(router_note.urls)),
    path("api/", include(router_activity.urls)),
]

urlpatterns += [
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(template_name="swagger-ui.html", url_name="schema"),
        name="swagger-ui",
    ),
]
