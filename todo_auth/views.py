from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import RegistrationSerializer
from django.contrib.auth import login, logout
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework import permissions
from django.views.decorators.csrf import csrf_exempt


@api_view(["POST"])
def Register_User(request):
    try:
        data = []
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.get(user=user)
            data = {"token":token.key}
            login(request, user)
        else:
            data = serializer.errors
        return Response(data)
    except Exception as e:
        return Response(e)

@csrf_exempt
@api_view(["POST"])
def Login_User(request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    token = Token.objects.get(user=user)
    login(request, user)
    return Response({"token": token.key})

@csrf_exempt
@api_view(["POST"])
def Logout_User(request):
    logout(request)
    return Response({"success":True})

  
        
