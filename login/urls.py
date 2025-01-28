

from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView

urlpatterns = [
    path('', LoginView.as_view(template_name='login/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),  # Logout
]

