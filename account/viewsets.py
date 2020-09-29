from .models import Account
from .serializers import AccountSerializer
from rest_framework import mixins,viewsets


class AccountList(mixins.ListModelMixin,viewsets.GenericViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class AccountDetail(mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,viewsets.GenericViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
