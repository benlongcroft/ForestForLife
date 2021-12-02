from django.shortcuts import render
from . import forms
from django.views.generic import CreateView
from django.urls import reverse_lazy


class Register(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'profiles/register.html'
