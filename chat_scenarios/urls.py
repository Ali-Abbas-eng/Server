from django.urls import path
from . import views

urlpatterns = [
    path('chat_scenarios/', views.chat_scenario_list, name='chat_scenario_list'),
]
