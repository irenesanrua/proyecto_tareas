from django.urls import path
from .import views

urlpatterns = [
    path('', views.index,name='index'),
    path('proyectos/listar',views.listar_proyectos, name='lista_proyectos'),
]