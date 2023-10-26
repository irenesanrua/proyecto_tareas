from django.urls import path
from .import views

urlpatterns = [
    path('', views.index,name='index'),
    path('proyectos/listar',views.listar_proyectos, name='lista_proyectos'),
    path('proyectos/<int:id_proyecto>/tareas/', views.dame_tareas_proyecto_porfecha, name='dame_tareas_proyecto_porfecha'),
    path('tarea/<int:id_tarea>/usuarios/', views.listar_usuarios_asignados, name='listar_usuarios_asignados'),

]