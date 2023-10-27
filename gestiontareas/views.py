from django.shortcuts import render
from .models import Proyecto, Tarea, Usuario, AsignacionTarea, Comentario
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