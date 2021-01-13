"""crmless URL Configuration"""

# from django.contrib import admin
from django.urls import path, include
import account.urls

urlpatterns = [
    path("api/", include("account.urls")),
]
