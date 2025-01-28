from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

class HistoricoView(TemplateView):
    template_name = 'historico.html'
