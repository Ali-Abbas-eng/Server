from django.contrib import admin
from django.urls import include, path
from .views import LoginView

urlpatterns = [
    path('api/v1/login/', LoginView.as_view(), name='account_login'),
]