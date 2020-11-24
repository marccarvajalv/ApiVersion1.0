from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import UsarioSerializer

class UsuarioApi(APIView):
    def post(self, request):
        serializer = UsarioSerializer(data = request.data)
        if serializer.is_valid():
            ##EN CASO DE ERROR AGREGAR UNA VARIABLE QUE SEA IGUAL A serializer.save()
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

