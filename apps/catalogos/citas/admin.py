from django.contrib import admin
from .models import TbCita

@admin.register(TbCita)
class TbCitaAdmin(admin.ModelAdmin):
    list_display = ('id', 'idpaciente', 'fecha', 'horaentrada', 'horasalida')
    search_fields = ('idpaciente__nombre', 'fecha')
    list_filter = ('fecha', 'horaentrada')
    ordering = ('-fecha', '-horaentrada')

    fieldsets = (
        (None, {
            'fields': ('idpaciente', 'fecha', 'horaentrada', 'horasalida')
        }),
    )
