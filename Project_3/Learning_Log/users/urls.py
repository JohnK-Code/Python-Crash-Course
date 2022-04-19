"""Define url patterns for users"""

from django.urls import path, include

from . import views

app_name = 'users'
urlpatterns = [
    path('', include('django.contrib.auth.urls')), # Include default auth urls
    path('register/', views.register, name='register'), # Registration page
]
