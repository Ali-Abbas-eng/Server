from django.contrib import admin
from django.urls import include, path
from .views import LoginView, RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('api/v1/login/', LoginView.as_view(), name='account_login'),
    path('api/v1/register/', RegisterView.as_view(), name='account_register'),
    path('api/v1/token/obtain/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
