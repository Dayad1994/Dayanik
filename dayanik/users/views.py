from django.views.generic import CreateView
from django.contrib.auth import views
from django.urls import reverse_lazy
from . import forms
from django.shortcuts import redirect


class SignUp(CreateView):
    form_class = forms.CreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class InlogView(views.LoginView):
    form_class = forms.AuthForm


class PwdChangeView(views.PasswordChangeView):
    form_class = forms.PwdChangeForm


class PwdResetView(views.PasswordResetView):
    form_class = forms.PwdResetForm


class PwdResetConfirmView(views.PasswordResetConfirmView):
    form_class = forms.PwdResetForm
