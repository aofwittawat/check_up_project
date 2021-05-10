from django.shortcuts import render
from .models import UserDetail


def Home(request):
    return render(request, 'home.html')


def Result(request):

    result = UserDetail.objects.last()

    return render(request, 'result.html', {'result': result})
