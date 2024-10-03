from django.db import models

class TbGenero(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    genero = models.CharField(db_column='Genero', max_length=9, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tb_Genero'
        verbose_name = 'Genero'
        verbose_name_plural = 'Generos'

