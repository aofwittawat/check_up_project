from django.urls import path, include
from .views import Home, Result


urlpatterns = [
    path('',Home,name='home-page'),
    path('result',Result,name='result-page'),
]
