from django.urls import path
from .views import hello_world
from rest_framework.routers import SimpleRouter
from .views import CourseModelViewSet

app_name = 'rest_api'
router = SimpleRouter(trailing_slash=False)
router.register('courses', CourseModelViewSet, basename='courses')
urlpatterns = [
    path('hello/', hello_world, name='hello_world_Api'),
]

urlpatterns += router.urls