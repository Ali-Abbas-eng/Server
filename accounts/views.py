from .serializers import CustomTokenSerializer, CustomLoginSerializer
from dj_rest_auth.views import LoginView as DefaultLoginView


class LoginView(DefaultLoginView):
    serializer_class = CustomLoginSerializer
    response_serializer = CustomTokenSerializer

    def get_response_serializer(self):
        return CustomTokenSerializer
