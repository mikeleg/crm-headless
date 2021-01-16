from rest_framework import serializers
from rest_framework import validators
from rest_framework.validators import UniqueValidator

from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    
    def validate_legalname(self, value):
        if not value:
            raise serializers.ValidationError("Legalname empty or missing")
        return value

    def validate_vat(self, value):
        if not value:
            raise serializers.ValidationError("Vat empty or missing")

        if Account.objects.filter(vat=value).count() > 0:
            raise serializers.ValidationError("Vat already exist")

        return value

    def validate_address(self, value):
        if not value:
            raise serializers.ValidationError("Address empty or missing")
        return value

    def validate_city(self, value):
        if not value:
            raise serializers.ValidationError("City empty or missing")
        return value

    def validate_zipcode(self, value):
        if not value:
            raise serializers.ValidationError("Zipcode empty or missing")
        return value

    def validate_country(self, value):
        if not value:
            raise serializers.ValidationError("Country empty or missing")
        return value

    def validate_province(self, value):
        if not value:
            raise serializers.ValidationError("Province empty or missing")
        return value

    def validate_phone(self, value):
        if not value:
            raise serializers.ValidationError("Phone empty or missing")
        return value

    def validate_email(self, value):
        if not value:
            raise serializers.ValidationError("Email empty or missing")
        return value

    def validate_type(self, value):
        if not value:
            raise serializers.ValidationError("Customer Type empty or missing")
        return value

    class Meta:
        model = Account
        fields = "__all__"
