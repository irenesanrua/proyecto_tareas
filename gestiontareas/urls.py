from django.urls import path, re_path
from .import views

urlpatterns = [
    path('', views.index,name='index'),
    path('proyectos/listar',views.listar_proyectos, name='lista_proyectos'),
    path('proyectos/<int:id_proyecto>/tareas/', views.dame_tareas_proyecto_porfecha, name='dame_tareas_proyecto_porfecha'),
    path('tarea/<int:id_tarea>/usuarios/', views.listar_usuarios_asignados, name='listar_usuarios_asignados'),
    path('tareas/usuario/<int:id_usuario>/<str:observaciones>', views.dame_tareas_observaciones, name='dame_tareas_observaciones'),
    path('tareas/anyos', views.mostrar_tareas_completadas_anios, name='mostrar_tareas_completadas_anios'),
    path('proyectos/<int:id_proyecto>/ultimocomentario', views.dame_ultimo_cliente_que_comento, name='dame_ultimo_cliente_que_comento'),
    path('tareas/<int:id_tarea>/<int:anyo>/<str:palabra>', views.dame_comentarios_tarea, name='dame_comentarios_tarea'),
    path('proyectos/<int:id_proyecto>/etiquetas', views.dame_etiquetas_tareas_proyecto, name='dame_etiquetas_tareas_proyecto'),
    path('tareas/<int:id_tarea>/usuarios', views.dame_usuarios_no_asignados_tarea, name='dame_usuarios_no_asignados_tarea'),
    path('usuarios/noasignados/', views.mostrar_usuarios_no_asignados, name='usuarios_no_asignados'),
]