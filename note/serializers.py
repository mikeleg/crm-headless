from rest_framework import serializers
from .models import Note


class NoteSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        note = Note(**validated_data)
        note.account_id = self.context["account_id"]
        note.lead_id = self.context["lead_id"]
        note.save()

        return note

    class Meta:
        model = Note
        fields = ["description"]
