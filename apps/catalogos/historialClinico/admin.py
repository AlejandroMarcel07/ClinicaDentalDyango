from django.contrib import admin
from .models import TbHistorialclinico

@admin.register(TbHistorialclinico)
class TbHistorialclinicoAdmin(admin.ModelAdmin):
    list_display = ('id', 'idcita', 'motivo', 'interpretacionradiografica', 'observacion', 'historiadeldolor')
    search_fields = ('id', 'motivo', 'interpretacionradiografica', 'observacion')
    list_filter = ('interpretacionradiografica',)
    ordering = ('id',)
