
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('login.urls')),  # Inclui as URLs do app de login
    path('home/', include('home.urls')),    # Inclui as URLs do app home
    path('historico/', include('historico.urls')),    # Inclui as URLs do app home
    path('', include('login.urls')),  # Adiciona a URL de login como a raiz do projeto
]