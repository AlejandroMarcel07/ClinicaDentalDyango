from django.db import models

from apps.catalogos.historialClinico.models import TbHistorialclinico
from apps.catalogos.tratamientoClinico.models import TbTratamientoclinico


class TbHistorialclinicotbTbTratamiento(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    idhistorialclinico = models.ForeignKey(TbHistorialclinico, models.DO_NOTHING, db_column='IdHistorialClinico')
    idtratamiento = models.ForeignKey(TbTratamientoclinico, models.DO_NOTHING, db_column='IdTratamiento')
    precio = models.DecimalField(db_column='Precio', max_digits=18, decimal_places=0)
# Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tb_HistorialClinicoTb_Tb_Tratamiento'
        verbose_name = 'Historial Clinico - Tratamiento'
        verbose_name_plural = 'Historiales Clinicos - Tratamientos'