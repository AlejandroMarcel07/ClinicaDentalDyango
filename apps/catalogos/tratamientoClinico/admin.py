from django.contrib import admin
from .models import TbTratamientoclinico

@admin.register(TbTratamientoclinico)
class TbTratamientoclinicoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombretratamiento')
    search_fields = ('nombretratamiento',)
    ordering = ('id',)
    list_per_page = 25