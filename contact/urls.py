from django.urls import include, path
from contact import viewsets

urlpatterns = [
    path("<accont_id:int>", viewsets.ContactCreateList.as_view()),
]
