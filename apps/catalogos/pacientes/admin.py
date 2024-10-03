from django.contrib import admin
from .models import TbPaciente

@admin.register(TbPaciente)
class TbPacienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombrecompleto', 'cedula', 'edad', 'idgenero', 'direccion', 'telefono', 'ocupacion', 'isdeleted')
    search_fields = ('nombrecompleto', 'cedula', 'telefono', 'ocupacion')
    list_filter = ('idgenero', 'edad', 'isdeleted')
    ordering = ('id',)
    list_per_page = 25


