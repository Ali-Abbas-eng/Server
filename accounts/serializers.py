from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from dj_rest_auth.serializers import TokenSerializer
from dj_rest_auth.models import TokenModel

User = get_user_model()


class CustomLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(style={'input_type': 'password'})

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password
        )

        if not user:
            msg = 'Unable to authenticate with provided credentials'
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number']  # add the fields you want to return here


class CustomTokenSerializer(TokenSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = TokenModel  # use Token here instead of TokenModel
        fields = ('key', 'user')

