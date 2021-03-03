from django.shortcuts import render
from .models import User
from django.http import JsonResponse

from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


class LogoutView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


def login_view(request):
    response_data = {
        'id': 1,
        'name': 'Login'
    }
    return JsonResponse(response_data)


def register_view(request):
    response_data = {
        'id': 2,
        'name': 'Register'
    }
    return JsonResponse(response_data)

# return render(request, "users/templates/registration/login.html")

