from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import Post


User = get_user_model()


def dayanik(request):
    return render(request, 'dayanik.html', {})


def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'text']
    success_url = reverse_lazy('posts:index')
    template_name = 'new_post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
