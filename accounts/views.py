from .serializers import TokenSerializer, LoginSerializer
from dj_rest_auth.views import LoginView as DefaultLoginView
from dj_rest_auth.registration.views import RegisterView as DefaultRegisterView
from .serializers import RegistrationSerializer


class LoginView(DefaultLoginView):
    serializer_class = LoginSerializer
    response_serializer = TokenSerializer

    def get_response_serializer(self):
        return TokenSerializer


class RegisterView(DefaultRegisterView):
    serializer_class = RegistrationSerializer
