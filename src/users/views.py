from django.shortcuts import render
from .models import User
from django.http import JsonResponse

# Create your views here.


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

