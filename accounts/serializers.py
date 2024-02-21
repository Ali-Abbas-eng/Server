from dj_rest_auth.serializers import LoginSerializer as DefaultLoginSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomLoginSerializer(DefaultLoginSerializer):
    def validate(self, attrs):
        attrs = super().validate(attrs)
        user = attrs['user']
        return {
            'user': UserSerializer(instance=user).data,
            'key': attrs['key'],
        }


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']  # add the fields you want to return here
