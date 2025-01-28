from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Página inicial protegida por login
class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'

