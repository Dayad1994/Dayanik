from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from django.views import generic

from .models import Post


User = get_user_model()


def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})
