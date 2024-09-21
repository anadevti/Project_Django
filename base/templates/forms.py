from django import forms
from base.models import Cadastrer
class CadastrerForm(forms.ModelForm):
    class Meta:
        model = Cadastrer
        fields = ['name', 'email', 'senha']
        widgets = {'senha': forms.PasswordInput()}