from rest_framework import serializers


class NoteResponse(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    description = serializers.CharField()
    customer_id = serializers.IntegerField(allow_null=True)


class UpsertNoteRequest(serializers.Serializer):
    id = serializers.IntegerField(
        allow_null=True,
        required=False,
    )
    description = serializers.CharField()
    customer_id = serializers.IntegerField(allow_null=True)
