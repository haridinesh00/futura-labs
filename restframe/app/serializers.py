from rest_framework import serializers

from app.models import District, Question

from rest_framework.authtoken.admin import User


class DistrictSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    pub_date = serializers.DateTimeField(format="%Y-%m-%dT%H:%M", read_only=True)

    class Meta:
        model = District
        fields = ['id', 'subject', 'description', 'pub_date']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['question_text', 'pub_date']


def create(self, validated_data):
    user = User.objects.create(username=validated_data['username'])
    user.set_password(validated_data['password'])
    user.save()
    return user
