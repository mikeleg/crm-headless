from rest_framework import serializers


class ContactResponse(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    surname = serializers.CharField(read_only=True)
    email = serializers.EmailField(read_only=True)
    phone = serializers.CharField(read_only=True)
    job_title = serializers.CharField(read_only=True)
    customer_id = serializers.IntegerField(read_only=True, allow_null=True)


class UpsertContactRequest(serializers.Serializer):
    id = serializers.IntegerField(
        allow_null=True,
        required=False,
    )
    name = serializers.CharField()
    surname = serializers.CharField()
    email = serializers.EmailField(allow_blank=True, allow_null=True)
    phone = serializers.CharField(allow_blank=True, allow_null=True)
    customer_id = serializers.IntegerField(allow_null=True)
