from rest_framework import serializers


class ActivityResponse(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    description = serializers.CharField(read_only=True)
    due_date = serializers.DateTimeField(read_only=True)
    customer_id = serializers.IntegerField(read_only=True, allow_null=True)


class UpsertActivityRequest(serializers.Serializer):
    id = serializers.IntegerField(
        allow_null=True,
        required=False,
    )
    description = serializers.CharField()
    due_date = serializers.DateTimeField(allow_null=True)
    customer_id = serializers.IntegerField(allow_null=True)
