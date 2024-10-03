from django.contrib import admin
from .models import TbExploracionclinica

@admin.register(TbExploracionclinica)
class TbExploracionclinicaAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo')
    search_fields = ('tipo',)
    ordering = ('tipo',)
