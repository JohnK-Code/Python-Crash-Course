"""Defines URL patterns for learning_logs"""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    path('', views.index, name="index"), # Home page
    path('topics/', views.topics, name='topics'), # Page that shows all topics
    path('topics/<int:topic_id>/', views.topic, name='topic'), # Detail page for a single topic
]