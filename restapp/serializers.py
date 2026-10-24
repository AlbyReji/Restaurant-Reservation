from django.contrib.auth.models import User
from rest_framework import serializers

from restapp.models import bookingdetails, contactdetails, restdetails


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "first_name", "last_name", "is_staff"]
        read_only_fields = ["id", "is_staff"]


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "email", "first_name", "last_name", "password"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class BookingDetailsSerializer(serializers.ModelSerializer):
    user_username = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = bookingdetails
        fields = ["id", "user", "user_username", "time", "date", "totalpeople"]
        read_only_fields = ["id", "user"]


class ContactDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = contactdetails
        fields = ["id", "Name", "Phone", "Email", "Subject"]
        read_only_fields = ["id"]


class RestDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = restdetails
        fields = ["id", "special", "opentime", "closetime"]
        read_only_fields = ["id"]
