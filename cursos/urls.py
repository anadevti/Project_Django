from django.urls import path
from cursos.views import create_course

app_name = 'Cursos'

urlpatterns = [
    path('course/', create_course, name='create_course')
]