from django.shortcuts import render
from .models import Proyecto, Tarea, Usuario, AsignacionTarea
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
    return render(request, 'asignaciontarea/listatareas_observacion.html', {'asignaciones': asignacionObservacion})