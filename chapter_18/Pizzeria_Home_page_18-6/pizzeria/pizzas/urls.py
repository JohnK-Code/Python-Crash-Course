"""Defines the URL patterns for the pizzas app"""

from django.urls import path

from . import views

app_name = 'pizzas'
urlpatterns = [
    path('', views.index, name="index")
]
