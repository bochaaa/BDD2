from rest_framework import serializers
from .models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = "__all__"

    def validate_dni(self, value):
        # Si querés permitir solo dígitos
        if not value.isdigit():
            raise serializers.ValidationError("El DNI debe contener solo números.")
        return value
