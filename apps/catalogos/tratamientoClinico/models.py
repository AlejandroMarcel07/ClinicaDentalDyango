from django.db import models

class TbTratamientoclinico(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    nombretratamiento = models.CharField(db_column='NombreTratamiento', max_length=100, db_collation='Modern_Spanish_CI_AS')

    class Meta:
        managed = False
        db_table = 'Tb_TratamientoClinico'
        verbose_name = 'Tratamiento Clinico'
        verbose_name_plural = 'Tratamientos Clinicos'