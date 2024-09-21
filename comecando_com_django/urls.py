from django.contrib import admin
from django.urls import path, include
from base.views import init, cadastrer

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', init),  # se eu nao coloco nada na url, ele chama a função init (atribuindo a url vazia como index)
    path('cadastrer/', cadastrer),  # se eu coloco /init na url, ele chama a função init
    path('course/', include('cursos.urls', namespace='courses'))
]