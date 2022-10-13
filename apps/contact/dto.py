from rest_framework import serializers


class ContactResponse(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nickname = serializers.CharField(read_only=True)
    name = serializers.CharField(read_only=True)
    surname = serializers.CharField(read_only=True)
    email = serializers.EmailField(read_only=True)
    phone = serializers.CharField(read_only=True)
    job_title = serializers.CharField(read_only=True)
    customer_id = serializers.IntegerField(read_only=True)


class UpsertContactRequest(serializers.Serializer):
    id = serializers.IntegerField(required=False, allow_null=True)
    nickname = serializers.CharField(required=False, allow_blank=True)
    name = serializers.CharField()
    surname = serializers.CharField()
    email = serializers.EmailField(required=False, allow_blank=True)
    phone = serializers.CharField(required=False, allow_blank=True)
    customer_id = serializers.IntegerField(required=False, allow_null=True)
    job_title = serializers.CharField(required=False, allow_blank=True, allow_null=True)
