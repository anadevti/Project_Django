from django import forms
from cursos.models import Curso
from datetime import date

class CourseForm(forms.ModelForm):
    def clean_date_of_course(self):
        data_of_the_course = self.cleaned_data['date_of_course']
        today = date.today()
        if data_of_the_course < today:
            raise forms.ValidationError('A Data não pode ser menor que a data atual')
        return data_of_the_course

    class Meta:
        model = Curso
        fields = '__all__'