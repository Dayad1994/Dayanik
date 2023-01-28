from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, ListView

from .models import Post
from .forms import PostForm


User = get_user_model()


def dayanik(request):
    return render(request, 'dayanik.html', {})


class BlogView(ListView):
    template_name = 'index.html'
    context_object_name = 'posts'
    queryset = Post.objects.all()


class ProfileView(DetailView, LoginRequiredMixin, CreateView):
    template_name = 'profile.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:index')

    def get_object(self):
        return get_object_or_404(User, username=self.kwargs['username'])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.get_object()
        context['profile'] = profile
        context['posts'] = Post.objects.filter(author=profile).all()
        return context
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


'''
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'text']
    success_url = reverse_lazy('posts:index')
    template_name = 'new_post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
'''
