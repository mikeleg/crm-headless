from .models import Account
from .serializers import AccountSerializer
from rest_framework import generics


class AccountList(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class AccountDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer