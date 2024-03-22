from django.http import JsonResponse
from .models import ChatScenario


def chat_scenario_list(request):
    scenarios = ChatScenario.objects.all()
    scenario_list = []
    for scenario in scenarios:
        scenario_list.append({
            "id": scenario.id,
            "socket_url": scenario.socket_url,
            "name": scenario.name,
            "description": scenario.description,
            "number_of_messages": scenario.number_of_messages,
            "background_url": request.build_absolute_uri(scenario.background_url),
            "image_url": request.build_absolute_uri(scenario.image_url),
        })
    return JsonResponse(scenario_list, safe=False)
