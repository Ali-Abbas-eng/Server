from django.http import JsonResponse
from .models import ChatScenario


def chat_scenario_list(request):
    scenarios = ChatScenario.objects.all()
    scenario_list = list(scenarios.values("id", "socket_url", "name", "description", "number_of_messages"))
    return JsonResponse(scenario_list, safe=False)
