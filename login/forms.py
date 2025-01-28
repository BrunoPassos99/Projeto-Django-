from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control rounded-pill',  # Bordas arredondadas
            'placeholder': 'Digite seu usuário',
            'id': 'id_username',
            'autocomplete': 'username'  # Sugestões do navegador
        }),
        label='',
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control rounded-pill',  # Bordas arredondadas
            'placeholder': 'Digite sua senha',
            'id': 'id_password',
            'autocomplete': 'current-password'  # Sugestões de senha
        }),
        label='',
    )
