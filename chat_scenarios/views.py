from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import ChatScenario


class ChatScenarioListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
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
        return Response(scenario_list)
