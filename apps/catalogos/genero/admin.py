from django.contrib import admin
from .models import TbGenero

class TbGeneroAdmin(admin.ModelAdmin):
    list_display = ('id', 'genero')
    search_fields = ('genero',)
    ordering = ('id',)

admin.site.register(TbGenero, TbGeneroAdmin)
