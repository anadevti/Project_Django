from django.contrib import admin
from base.models import Cadastrer

@admin.register(Cadastrer)
class CadastrerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'data')
    search_fields = ('name', 'email')
    list_filter = ('data',)
