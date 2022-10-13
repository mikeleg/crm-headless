from rest_framework import serializers
from core.enums import CUSTOMER_TYPE


class CustomerResponse(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nickname = serializers.CharField(read_only=True)
    legalname = serializers.CharField(read_only=True)
    vat = serializers.CharField(read_only=True)
    address = serializers.CharField(read_only=True)
    city = serializers.CharField(read_only=True)
    zipcode = serializers.CharField(read_only=True)
    country = serializers.CharField(read_only=True)
    province = serializers.CharField(read_only=True)
    geo = serializers.CharField(read_only=True)
    phone = serializers.CharField(read_only=True)
    email = serializers.CharField(read_only=True)
    pec = serializers.CharField(read_only=True)
    sdi = serializers.CharField(read_only=True)
    type = serializers.ChoiceField(choices=CUSTOMER_TYPE.choices, read_only=True)


class UpsertCustomerRequest(serializers.Serializer):
    id = serializers.IntegerField(
        allow_null=True,
        required=False,
    )
    nickname = serializers.CharField()
    legalname = serializers.CharField()
    address = serializers.CharField(allow_blank=True)
    vat = serializers.CharField(allow_blank=True)
    city = serializers.CharField(allow_blank=True)
    zipcode = serializers.CharField(allow_blank=True)
    country = serializers.CharField(allow_blank=True)
    province = serializers.CharField(allow_blank=True)
    geo = serializers.CharField(allow_blank=True)
    phone = serializers.CharField(allow_blank=True)
    email = serializers.CharField(allow_blank=True)
    pec = serializers.CharField(allow_blank=True)
    sdi = serializers.CharField(allow_blank=True)
    type = serializers.ChoiceField(choices=CUSTOMER_TYPE.choices)
