from django.contrib import admin
from .models import Usuario, Tarea, Proyecto, Etiqueta, EtiquetaAsociada, ProyectoAsignado, Comentario, AsignacionTarea

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Tarea)
admin.site.register(Proyecto)
admin.site.register(Etiqueta)
admin.site.register(EtiquetaAsociada)
admin.site.register(ProyectoAsignado)
admin.site.register(Comentario)
admin.site.register(AsignacionTarea)