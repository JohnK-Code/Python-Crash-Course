"""Defines the URL patterns for the pizzas app"""

from django.urls import path

from . import views

app_name = 'pizzas'
urlpatterns = [
    path('', views.index, name="index"), # Home page
    path('pizzas/', views.pizzas, name='pizzas'), # Page that shows all pizzas
    path('pizzas/<int:pizza_id>/', views.toppings, name='toppings'), # Page that show all toppings for a pizza
]
