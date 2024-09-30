from django.shortcuts import render
from cursos.forms import CourseForm
from cursos.models import Curso
from django.views.decorators.cache import cache_page

@cache_page(30)
def create_course(request):
    courses = Curso.objects.all()
    form = CourseForm(request.POST or None)
    success = False
    if form.is_valid():
        form.save()
        success = True
    context = {
        'form': form,
        'sucesss': success,
        'courses': courses
        }
    return render(request, 'form.html', context)