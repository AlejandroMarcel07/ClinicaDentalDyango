from django.db import models

from apps.catalogos.genero.models import TbGenero


class TbPaciente(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    nombrecompleto = models.CharField(db_column='NombreCompleto', max_length=60, db_collation='Modern_Spanish_CI_AS')
    cedula = models.CharField(db_column='Cedula', max_length=16, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    edad = models.IntegerField(db_column='Edad')
    idgenero = models.ForeignKey(TbGenero, models.DO_NOTHING, db_column='IdGenero')
    direccion = models.CharField(db_column='Direccion', max_length=100, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    telefono = models.IntegerField(db_column='Telefono', blank=True, null=True)
    ocupacion = models.CharField(db_column='Ocupacion', max_length=20, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    antecedentes = models.TextField(db_column='Antecedentes', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    isdeleted = models.BooleanField(db_column='IsDeleted', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Tb_Paciente'
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'