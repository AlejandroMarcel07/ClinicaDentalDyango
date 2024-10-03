from django.contrib import admin
from .models import TbRecetamedica

@admin.register(TbRecetamedica)
class TbRecetamedicaAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_idcita', 'descripcion')
    search_fields = ('id', 'descripcion')
    list_filter = ('idcita',)
    ordering = ('id',)
    list_per_page = 25


    def get_idcita(self, obj):
        return f"Cita ID: {obj.idcita.id}" if obj.idcita else "Sin Cita"
    get_idcita.short_description = 'Cita'
    get_idcita.admin_order_field = 'idcita__id'
