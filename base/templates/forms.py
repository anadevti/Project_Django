from django import forms

class CadastrerForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    senha = forms.CharField(widget=forms.PasswordInput, label='Senha', max_length=100)