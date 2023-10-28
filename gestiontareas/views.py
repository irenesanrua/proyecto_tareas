from django.shortcuts import render
from .models import Proyecto, Tarea, Usuario, AsignacionTarea, Comentario, Etiqueta
from django.db.models import Q

# Create your views here.

def index(request):
    return render(request, 'index.html')

def listar_proyectos(request):
    proyectos=Proyecto.objects.select_related("creador").select_related("tareas").prefetch_related("usuarios")
    proyectos=Proyecto.objects.all()
    return render(request, 'proyecto/lista.html', {"proyectos_mostrar": proyectos})

def dame_tareas_proyecto_porfecha(request, id_proyecto):
    proyecto = Proyecto.objects.get(id=id_proyecto)
    tareas = Tarea.objects.filter(proyecto=proyecto).order_by("-fecha_creacion")
    return render(request, 'tarea/lista.html', {"tareasproyecto_mostrar": tareas, "proyecto": proyecto})

def listar_usuarios_asignados(request, id_tarea):
    tarea = Tarea.objects.get(id=id_tarea)
    asignaciones = AsignacionTarea.objects.filter(tarea=tarea).order_by('fecha_asignacion')
    return render(request, 'asignaciontarea/listausuarios.html', {'asignaciones': asignaciones, 'tarea': tarea})

def dame_tareas_observaciones(request, id_usuario,observaciones):
    asignacionObservacion = AsignacionTarea.objects.filter(observaciones__contains=observaciones).filter(usuario=id_usuario)
    return render(request, 'asignaciontarea/listatareas_observacion.html', {'mostrar_asignaciones': asignacionObservacion})

def mostrar_tareas_completadas_anios(request):
    anyo_inicio = int(request.GET.get('anyo_inicio', 2021))
    anyo_fin = int(request.GET.get('anyo_fin', 2023))
    # Filtra las tareas creadas entre los dos años y con estado "Completada"
    tareas = Tarea.objects.filter(fecha_creacion__year__gte=anyo_inicio, fecha_creacion__year__lte=anyo_fin, tipoestado="COM")
    return render(request, 'tarea/lista_tareas_entre_anios.html', {'tareas': tareas, 'anyo_inicio': anyo_inicio, 'anyo_fin': anyo_fin})

def dame_ultimo_cliente_que_comento(request, id_proyecto):
    proyecto = Proyecto.objects.get(id=id_proyecto)
    # Obtén la última tarea del proyecto
    ultima_tarea = Tarea.objects.filter(proyecto=proyecto).order_by("-fecha_creacion")[:1].get() #se puede usar latest() para coger el último
    # Obtén el último comentario en la última tarea
    ultimo_comentario = Comentario.objects.filter(tarea=ultima_tarea).order_by("-fecha_comentario")[:1].get()
    return render(request, 'comentarios/ultimo.html', {'proyecto': proyecto, 'mostrar_autor': ultimo_comentario})

def dame_comentarios_tarea(request, id_tarea, anyo, palabra):
    tarea = Tarea.objects.get(id=id_tarea)
    comentarios= Comentario.objects.filter(tarea=tarea).filter(fecha_comentario__year=anyo, contenido__startswith=palabra)
    return render(request, 'comentarios/lista_portarea.html', {'tarea':tarea, 'comentario': comentarios})

def dame_etiquetas_tareas_proyecto(request, id_proyecto):
    proyecto = Proyecto.objects.get(id=id_proyecto)
    tareas = Tarea.objects.filter(proyecto=proyecto)
    etiquetas= Etiqueta.objects.filter(tareas__in= tareas).distinct()
    return render(request, 'etiquetas/lista_tareasproyecto.html', {"tareas": tareas, "proyecto": proyecto, "etiquetas": etiquetas})

def dame_usuarios_no_asignados_tarea(request, id_tarea):
    tarea= Tarea.objects.get(id=id_tarea)
    usuarios = AsignacionTarea.objects.filter(tarea=tarea).filter(usuario= None)
    return render(request, 'tarea/usuariosnoasignados.html', {'usuarios': usuarios, 'tarea': tarea})

def mostrar_usuarios_no_asignados(request):
    # Obtén todos los usuarios
    usuarios = Usuario.objects.all()
    # Filtra las tareas asignadas
    tareas_asignadas = AsignacionTarea.objects.values('usuario_id').distinct()
    # Filtra los usuarios que no están asignados a ninguna tarea
    usuarios_no_asignados = Usuario.objects.exclude(id__in=tareas_asignadas)
    return render(request, 'tarea/usuariosNOasigna2.html', {'usuarios_no_asignados': usuarios_no_asignados})

#Páginas de error
def error_404(request, exception=None):
    return render(request, 'errores/404.html', None,None,404)

def error_500(request, exception=None):
    return render(request, 'errores/500.html', None,None,500)

def error_400(request, exception=None):
    return render(request, 'errores/400.html', None,None,400)

def error_403(request, exception=None):
    return render(request, 'errores/403.html', None,None,403)