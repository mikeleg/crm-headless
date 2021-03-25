from rest_framework import serializers
from .models import Contact
from rest_framework import serializers


class ContactSerializer(serializers.ModelSerializer):
    def validate(self, data):
        if len(data["phone"]) == 0 and len(data["email"]) == 0:
            raise serializers.ValidationError("phone or email are mandatory")
        return data
        
    class Meta:
        model = Contact
        fields = "__all__"
        read_only_fields = ["id"]
