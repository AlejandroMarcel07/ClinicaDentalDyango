from django.db import models
from apps.catalogos.citas.models import TbCita


class TbFactura(models.Model):
    idfactura = models.AutoField(db_column='IdFactura', primary_key=True)
    idcita = models.ForeignKey(TbCita, models.DO_NOTHING, db_column='IdCita')
    costototal = models.DecimalField(db_column='CostoTotal', max_digits=18, decimal_places=0)
    tipopago = models.CharField(db_column='TipoPago', max_length=50, db_collation='Modern_Spanish_CI_AS')
    descuentoaplicado = models.BooleanField(db_column='DescuentoAplicado')
    montodescuento = models.DecimalField(db_column='MontoDescuento', max_digits=18, decimal_places=0, blank=True, null=True)
    pagounico = models.BooleanField(db_column='PagoUnico')
    cantidadcuotas = models.IntegerField(db_column='CantidadCuotas', blank=True, null=True)
    cuotaspagadas = models.IntegerField(db_column='CuotasPagadas', blank=True, null=True)
    costoporcuota = models.DecimalField(db_column='CostoPorCuota', max_digits=18, decimal_places=0, blank=True, null=True)
    cancelado = models.BooleanField(db_column='Cancelado')
    totaldescuentoaplicado = models.DecimalField(db_column='TotalDescuentoAplicado', max_digits=18, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Tb_Factura'
        verbose_name = 'Factura'
        verbose_name_plural = 'Facturas'
