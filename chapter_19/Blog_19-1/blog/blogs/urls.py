import django


from django.urls import path

from . import views

app_name = 'blogs'
urlpatterns = [
    path('', views.index, name='home'), # Page for showing all blog posts
    path('new_post/', views.new_post, name='new_post'), # Page for submitting new post
    path('edit_post/<int:blogpost_id>', views.edit_post, name='edit_post'), # Page for editing blog posts
]
