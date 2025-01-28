from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'login/login.html'  # Define o template a ser usado
    redirect_authenticated_user = True  # Redireciona usuários autenticados para a home, se já estiverem logados

    def form_valid(self, form):
        """Personalize o comportamento após o formulário de login ser validado."""
        # Isso pode ser expandido se você quiser adicionar lógica adicional após o login
        return super().form_valid(form)
