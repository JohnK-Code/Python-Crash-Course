"""Define URL patterns for users app"""

from django.urls import path, include

from . import views
app_name = 'users'
urlpatterns = [
    path('', include('django.contrib.auth.urls')), # Default auth urls
    path('register/', views.register, name='register'), # Registration page
]