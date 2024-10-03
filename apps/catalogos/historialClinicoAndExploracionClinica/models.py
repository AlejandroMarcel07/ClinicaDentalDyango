from django.db import models

from apps.catalogos.exploracionClinica.models import TbExploracionclinica
from apps.catalogos.historialClinico.models import TbHistorialclinico


class TbHistorialclinicotbExploracionclinica(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    idhistorialclinico = models.ForeignKey(TbHistorialclinico, models.DO_NOTHING, db_column='IdHistorialClinico')
    idexploracionclinica = models.ForeignKey(TbExploracionclinica, models.DO_NOTHING, db_column='IdExploracionClinica')

    class Meta:
        managed = False
        db_table = 'Tb_HistorialClinicoTb_ExploracionClinica'
        verbose_name = 'Historial Clinico - Exploracion Clinica'
        verbose_name_plural = 'Historiales Clinicos - Exploraciones Clinicas'