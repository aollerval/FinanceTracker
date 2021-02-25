from django.urls import path

from . import views
from .classes import mainFunctions

urlpatterns = [
    path('', views.index, name='index'),
    path('LoginForm', mainFunctions.printLoginForm, name = 'LoginForm'),
]