from rest_framework import serializers

from app.models import District

from rest_framework.authtoken.admin import User


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ['subject', 'description']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']


def create(self, validated_data):
    user = User.objects.create(username=validated_data['username'])
    user.set_password(validated_data['password'])
    user.save()
    return user
