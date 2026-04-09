from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UsuarioSerializer
from django.contrib.auth import authenticate

@api_view(['GET'])
def list_usuario(request):

    usuarios = User.objects.all()
    serializer = UsuarioSerializer(usuarios, many=True)

    return Response(serializer.data)


@api_view(['POST'])
def login_usuario(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)
    serializer = UsuarioSerializer(user)
    if user is not None:
        return Response({
            "success": True,
            "user" : serializer.data,
        })
    return Response({
            "success": False,
            "message": "Credenciales incorrectas"
        }, status=401)
