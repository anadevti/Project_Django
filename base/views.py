from django.shortcuts import render
from django.http import HttpResponse
from base.templates.forms import CadastrerForm
from base.models import Cadastrer
def init(request):
    return render(request, 'init.html')

def cadastrer(request):
    success = False
    form = CadastrerForm(request.POST or None)
    if form.is_valid():
            success = True
            form.save()
    context = {
        'form': form,
        'sucesss': success
    }
    return render (request, 'cadastrer.html', context)