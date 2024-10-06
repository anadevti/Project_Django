import pytest
from model_bakery import baker
from cursos.models import Curso

@pytest.fixture # it will be used in the test below
def course():
    course = baker.make(
        Curso,
        title='Curso de Python',
        level='B',
        carg_hours=40,
    )
    return course


@pytest.mark.django_db
def test_str_return_string(course):
    assert str(course) == 'Curso de Python - Básico - 40 horas'