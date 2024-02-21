from .serializers import UserSerializer
from dj_rest_auth.views import LoginView as DefaultLoginView
from dj_rest_auth.serializers import TokenSerializer
from dj_rest_auth.models import TokenModel

class CustomTokenSerializer(TokenSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = TokenModel  # use Token here instead of TokenModel
        fields = ('key', 'user')

class LoginView(DefaultLoginView):
    def get_response_serializer(self):
        return CustomTokenSerializer
