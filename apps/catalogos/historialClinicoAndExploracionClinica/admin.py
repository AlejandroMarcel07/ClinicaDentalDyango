from django.contrib import admin
from .models import TbHistorialclinicotbExploracionclinica

@admin.register(TbHistorialclinicotbExploracionclinica)
class TbHistorialclinicotbExploracionclinicaAdmin(admin.ModelAdmin):
    list_display = ('id', 'idhistorialclinico', 'idexploracionclinica')
    search_fields = ('idhistorialclinico__id', 'idexploracionclinica__id')
    list_filter = ('idhistorialclinico', 'idexploracionclinica')
    ordering = ('id',)
