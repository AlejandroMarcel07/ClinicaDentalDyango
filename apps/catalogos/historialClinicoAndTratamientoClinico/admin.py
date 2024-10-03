from django.contrib import admin
from .models import TbHistorialclinicotbTbTratamiento

@admin.register(TbHistorialclinicotbTbTratamiento)
class TbHistorialclinicotbTbTratamientoAdmin(admin.ModelAdmin):
    list_display = ('id', 'idhistorialclinico', 'idtratamiento', 'precio')
    search_fields = ('idhistorialclinico__id', 'idtratamiento__id')
    list_filter = ('idhistorialclinico', 'idtratamiento')
    ordering = ('id',)
