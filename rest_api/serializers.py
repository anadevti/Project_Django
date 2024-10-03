from rest_framework.serializers import ModelSerializer
from cursos.models import Curso

class CourseModelSerializer(ModelSerializer):
    class Meta:
        model = Curso
        fields = ['id', 'codigo', 'descricao', 'nivel', 'ativo']