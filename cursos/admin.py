from django.contrib import admin
from cursos.models import Curso
# Register your models here.

@admin.register(Curso)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'level', 'carg_hours', 'date_of_course', 'description')
    search_fields = ('title', 'level', 'date_of_course')
    list_filter = ('level', 'date_of_course')
    date_hierarchy = 'date_of_course'
    ordering = ('-date_of_course',)