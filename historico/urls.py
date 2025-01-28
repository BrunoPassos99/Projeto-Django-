from django.urls import path
from .views import HistoricoView

urlpatterns = [
    path('historico/', HistoricoView.as_view(), name='historico'),
]
