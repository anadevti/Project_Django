from django import forms
from cursos.models import Curso

class CourseForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'
      #  widgets = {
       #     'date_of_course': forms.DateInput(format='%d/%m/%Y', attrs={'class': 'form-control', 'placeholder': 'dd/mm/aaaa'}),
     #   }