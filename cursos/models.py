from django.db import models

# Create your models here.

class Curso(models.Model):
    levels_of_course = (
        ('B', 'Básico'),
        ('I', 'Intermediario'),
        ('A', 'Avançado'),
    )
    title = models.CharField(max_length=100)
    level = models.CharField(max_length=1, choices=levels_of_course)
    carg_hours = models.IntegerField()
    date_of_course = models.DateField(help_text='Formato: dd/mm/aaaa')
    description = models.TextField()

    def __str__(self):
        return f'{self.title} - {self.get_level_display()} - {self.carg_hours} horas'

    class Meta:
        verbose_name = 'Cadastros de Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['-date_of_course']