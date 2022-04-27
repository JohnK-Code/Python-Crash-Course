from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import BlogPost
from .forms import PostForm

# Create your views here.
def index(request):
    """Home page for Blog"""
    posts = BlogPost.objects.all().order_by('-date_added')
    context = {'posts': posts}
    return render(request, 'blogs/index.html', context)

@login_required
def new_post(request):
    """Page for submitting new post"""
    if request.method != 'POST':
        # No data submitted; create a blank form
        form = PostForm()
    else:
        # Post data submitted; process data
        form = PostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            return redirect('blogs:home')
    
    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)

@login_required
def edit_post(request, blogpost_id):
    """Edit existing post"""
    #post = BlogPost.objects.get(id=blogpost_id) - replaced by get_object_or_404
    post = get_object_or_404(BlogPost ,id=blogpost_id)
    check_post_owner(request, post)

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

def check_post_owner(request, post):
    """Check current user is post owner"""
    if post.owner != request.user:
        raise Http404