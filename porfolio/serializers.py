from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Usuario


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Usuario
        fields = "__all__"

    def create(self, validated_data):
        # Extract the password from validated data
        password = validated_data.pop("password")

        # Create the user with the rest of the validated data
        user = Usuario(**validated_data)

        # Hash the password
        user.password = make_password(password)

        # Save the user
        user.save()

        return user
