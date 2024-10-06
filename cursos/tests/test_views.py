from http.client import responses
from pytest_django.asserts import assertTemplateUsed
import pytest

@pytest.mark.django_db
def test_course_view_return_template(client):
    response = client.get('/course/course/')
    assert response.status_code == 200
    assertTemplateUsed(response, 'form.html')