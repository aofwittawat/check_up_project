from django.shortcuts import render
from .models import UserDetail


def Home(request):
    return render(request,'home.html')

def Result(request, username):
    result = UserDetail.objects.filter(username=username)
    for r in result:
        HT = UserDetail.objects.filter(HT=True)
        r.risk = HT
        

    context = {'result':result}
    return render(request, 'result.html', context)

def navbar(request):
    user = UserDetail.objects.all()
    print(user)
    return render(request, 'navbar.html', {'user':user})