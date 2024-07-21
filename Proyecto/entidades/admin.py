from django.contrib import admin
from .models import Profesor, Estudiante

class CursoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "comision")
    list_filter = ("nombre",)




# Register your models here.

@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email', 'fecha_nacimiento', 'asistencia', 'faltas')  # Campos que se mostrarán en la lista de estudiantes
    search_fields = ('nombre', 'apellido', 'email')  # Campos por los cuales se puede buscar un estudiante
    list_filter = ('asistencia', 'faltas')  # Filtros laterales en la interfaz de administración
# core/admin.py
from django.contrib import admin
from .models import Profesor

class ProfesorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email', 'telefono')

admin.site.register(Profesor, ProfesorAdmin)
