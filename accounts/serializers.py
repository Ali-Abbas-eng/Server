from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from dj_rest_auth.serializers import TokenSerializer as DefaultTokenSerializer
from dj_rest_auth.registration.serializers import RegisterSerializer as DefaultRegistrationSerializer
from dj_rest_auth.models import TokenModel
from .forms import CustomUserCreationForm

User = get_user_model()


class LoginSerializer(serializers.Serializer):
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


class TokenSerializer(DefaultTokenSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = TokenModel  # use Token here instead of TokenModel
        fields = ('key', 'user')


class RegistrationSerializer(DefaultRegistrationSerializer):
    username = None
    phone_number = serializers.CharField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    def get_cleaned_data(self):
        return {
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'phone_number': self.validated_data.get('phone_number', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'password2': self.validated_data.get('password2', '')
        }

    def save(self, request):
        cleaned_data = self.get_cleaned_data()
        form = CustomUserCreationForm(cleaned_data)
        if not form.is_valid():
            raise serializers.ValidationError(form.errors)
        user = form.save()
        return user
