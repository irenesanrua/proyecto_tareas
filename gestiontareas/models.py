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
    titulo = models.TextField(max_length=200)
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
    hora_vencimiento= models.DateTimeField(default=timezone.now, blank=True, null=True)

class Proyecto(models.Model):

    nombre= models.TextField(max_length=200)
    descripcion = models.TextField()
    duracion_estimada= models.FloatField()
    fecha_inicio= models.DateTimeField(default=timezone.now, blank=True, null=True) 
    fecha_finalizacion= models.DateTimeField(default=timezone.now, blank=True, null=True)

class Etiqueta(models.Model):
    nombre = models.TextField(max_length=200, unique=True)

class AsignaciónTarea(models.Model):
    observaciones=models.TextField()
    fecha_asignacion= models.DateTimeField(default=timezone.now, blank=True, null=True)

class Comentario(models.Model):
    contenido= models.TextField()
    fecha_comentario: models.DateTimeField(default=timezone.now, blank=True, null=True)



