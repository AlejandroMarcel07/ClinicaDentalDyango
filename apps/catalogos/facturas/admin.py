from django.contrib import admin
from .models import TbFactura

@admin.register(TbFactura)
class TbFacturaAdmin(admin.ModelAdmin):
    list_display = ('idfactura', 'idcita', 'costototal', 'tipopago', 'descuentoaplicado', 'montodescuento', 'pagounico', 'cantidadcuotas', 'cuotaspagadas', 'costoporcuota', 'cancelado', 'totaldescuentoaplicado')
    search_fields = ('idfactura', 'tipopago')
    list_filter = ('descuentoaplicado', 'pagounico', 'cancelado')
    ordering = ('idfactura',)
