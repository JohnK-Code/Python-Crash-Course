from dataclasses import fields
from logging import PlaceHolder
from turtle import title
from django import forms

from .models import BlogPost

class PostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':''}), label='')
    class Meta:
        model = BlogPost
        fields = ['title', 'text']
        labels = {'text': ''}