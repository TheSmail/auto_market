from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import ClientListSerializer

class ClientListView(APIView):

    def get(self, request):
        clients = Client.objects.all()
        serializer = ClientListSerializer(clients, many=True)
        return Response(serializer.data)
