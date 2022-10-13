from rest_framework import serializers

from core.enums import ADDRESS_TYPE


class AddressResponse(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    customer_id = serializers.IntegerField(read_only=True)
    concat_id = serializers.IntegerField(read_only=True)
    nickname = serializers.CharField(read_only=True)
    street = serializers.CharField(read_only=True)
    number = serializers.IntegerField(read_only=True)
    city = serializers.CharField(read_only=True)
    zip_code = serializers.CharField(read_only=True)
    country = serializers.CharField(read_only=True)
    type = serializers.ChoiceField(choices=ADDRESS_TYPE.choices, read_only=True)


class UpsertAddressRequest(serializers.Serializer):
    id = serializers.IntegerField(
        allow_null=True,
        required=False,
    )
    customer_id = serializers.IntegerField(allow_null=True, required=False)
    contact_id = serializers.IntegerField(allow_null=True, required=False)
    nickname = serializers.CharField(allow_null=True)
    street = serializers.CharField(allow_null=True)
    number = serializers.IntegerField(allow_null=True)
    city = serializers.CharField(allow_null=True)
    zip_code = serializers.CharField(allow_null=True)
    country = serializers.CharField(allow_null=True)
    type = serializers.ChoiceField(choices=ADDRESS_TYPE.choices, allow_null=True)
