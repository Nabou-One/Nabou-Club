from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_club, name='hello_club'),
]
