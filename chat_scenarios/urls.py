from django.urls import path
from . import views

urlpatterns = [
    path('chat_scenarios/', views.ChatScenarioListView.as_view(), name='chat_scenario_list'),
]
