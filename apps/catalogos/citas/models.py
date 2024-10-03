from django.db import models
from apps.catalogos.pacientes.models import TbPaciente


class TbCita(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    idpaciente = models.ForeignKey(TbPaciente, models.DO_NOTHING, db_column='IdPaciente')
    fecha = models.DateField(db_column='Fecha')
    horaentrada = models.TimeField(db_column='HoraEntrada')
    horasalida = models.TimeField(db_column='HoraSalida')

    class Meta:
        managed = False
        db_table = 'Tb_Cita'
        verbose_name = 'Cita'
        verbose_name_plural = 'Citas'
