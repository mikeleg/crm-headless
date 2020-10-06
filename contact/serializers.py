from rest_framework import serializers
from .models import Contact


class ContactSerializer(serializers.ModelSerializer):
    
    def validate(self, data):
        if data["laed_id"] > 0 and data["account_id"] > 0:
            raise serializers.ValidationError("contact isn't in account and lead simultaneously")
        
        if len(data["phone"]) == 0 and len(data["email"]) == 0:
            raise serializers.ValidationError("phone or email are mandatory")
        return data

    def create(self, validated_data):
        contact = Contact(**validated_data)
        contact.account_id = self.context["account_id"]
        contact.lead_id = self.context["lead_id"]
        contact.save()

        return contact

    class Meta:
        model = Contact
        fields = ["id", "name", "surname", "email", "phone", "default", "jobTitle"]
