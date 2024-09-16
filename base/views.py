from django.shortcuts import render
from django.http import HttpResponse
from base.templates.forms import CadastrerForm

def init(request):
    return render(request, 'init.html')

def cadastrer(request):
    success = False
    if request.method == 'GET':
        form = CadastrerForm()
    else:
        form = CadastrerForm(request.POST)
        if form.is_valid():
            success = True
    context = {
        'form': form,
        'sucesss': success
    }
    return render (request, 'cadastrer.html', context)