"""crmless URL Configuration"""

# from django.contrib import admin
from django.urls import path, include
import account.urls
import contact.urls
import note.urls

urlpatterns = [
    path("api/", include("account.urls")),
    path("api/", include("contact.urls")),
    path("api/", include("note.urls")),
]
