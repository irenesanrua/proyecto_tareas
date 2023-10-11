from django.conf import settings
from django.db import models
from django.utils import timezone

#Create your models here

class Usuario(models.Model):
    nombre = models.TextField(max_length=200, unique=True)
    correo_electronico = models.TextField(max_length=300)
    contraseña = models.TextField()
    fecha_registro = models.DateTimeField(default=timezone.now, blank=True, null=True)
    
class Tarea(models.Model):
    titulo = models.TextField(max_length=100)
    descripcion = models.TextField()
    prioridad= models.IntegerField()
    ESTADO=[
        ('PEND', 'Pendiente'),
        ('PROG', 'Progreso'),
        ('COMP', 'Completada'),
    ]
    tipoestado = models.CharField(
        max_length=4,
        choices=ESTADO,
        default='PEND',)
    completada=models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(default=timezone.now, blank=True, null=True)
    hora_vencimiento= models.TimeField(default=timezone.now)
    creador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="creadores")
    usuario = models.ManyToManyField(Usuario, through="AsignacionTarea", related_name="usuario2")

class Proyecto(models.Model):
    nombre= models.TextField(max_length=200)
    descripcion = models.TextField()
    duracion_estimada= models.FloatField()
    fecha_inicio= models.DateTimeField(default=timezone.now, blank=True, null=True) 
    fecha_finalizacion= models.DateTimeField(default=timezone.now, blank=True, null=True)
    creador = models.ForeignKey(Usuario, on_delete = models.CASCADE, related_name="creador")
    usuarios = models.ManyToManyField(Usuario, through="ProyectoAsignado",related_name="usuario")
    tareas = models.ForeignKey(Tarea, on_delete=models.CASCADE)

class Etiqueta(models.Model):
    nombre = models.TextField(max_length=200, unique=True, blank=True)
    tareas = models.ManyToManyField(Tarea, through="EtiquetaAsociada")

class AsignacionTarea(models.Model):
    observaciones=models.TextField()
    fecha_asignacion= models.DateTimeField(default=timezone.now, blank=True, null=True)
    tareas= models.ForeignKey(Tarea, on_delete=models.CASCADE)
    usuarios= models.ForeignKey(Usuario, on_delete=models.CASCADE)

class Comentario(models.Model):
    contenido= models.TextField()
    fecha_comentario: models.DateTimeField(default=timezone.now, blank=True, null=True)
    autor = models.OneToOneField(Usuario, on_delete = models.CASCADE)
    tareas= models.OneToOneField(Tarea, on_delete=models.CASCADE)

class ProyectoAsignado(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)

class EtiquetaAsociada(models.Model):
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    etiqueta = models.ForeignKey(Etiqueta, on_delete=models.CASCADE)