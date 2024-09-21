from django.shortcuts import render
from cursos.forms import CourseForm
# Create your views here.

def create_course(request):
    form = CourseForm(request.POST or None)
    success = False
    if form.is_valid():
        form.save()
        success = True
    context = {
        'form': form,
        'sucesss': success
        }
    return render(request, 'form.html', context)