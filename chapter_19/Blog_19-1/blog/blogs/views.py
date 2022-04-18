from multiprocessing import context
from turtle import pos
from django.shortcuts import render, redirect

from .models import BlogPost
from .forms import PostForm

# Create your views here.
def index(request):
    """Home page for Blog"""
    posts = BlogPost.objects.all().order_by('-date_added')
    context = {'posts': posts}
    return render(request, 'blogs/index.html', context)

def new_post(request):
    """Page for submitting new post"""
    if request.method != 'POST':
        # No data submitted; create a blank form
        form = PostForm()
    else:
        # Post data submitted; process data
        form = PostForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:home')
    
    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)

def edit_post(request, blogpost_id):
    """Edit existing post"""
    post = BlogPost.objects.get(id=blogpost_id)

    if request.method != 'POST':
        # Initial request; pre-fill form with the current post
        form = PostForm(instance=post)
    else:
        # POST data submitted; process data
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:home')
    
    context = {'post': post, 'form': form}
    return render(request, 'blogs/edit_post.html', context)