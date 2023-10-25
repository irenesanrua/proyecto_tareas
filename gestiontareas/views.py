from django.shortcuts import render
from .models import Proyecto, Tarea

# Create your views here.

def index(request):
    return render(request, 'index.html')

def listar_proyectos(request):
    proyectos=Proyecto.objects.select_related("creador").select_related("tareas").prefetch_related("usuarios")
    proyectos=Proyecto.objects.all()
    return render(request, 'proyecto/lista.html', {"proyectos_mostrar": proyectos})