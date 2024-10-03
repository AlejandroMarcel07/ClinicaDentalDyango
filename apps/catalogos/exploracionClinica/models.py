from django.db import models

class TbExploracionclinica(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    tipo = models.CharField(db_column='Tipo', max_length=100, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tb_ExploracionClinica'
        verbose_name = 'Exploración Clínica'
        verbose_name_plural = 'Exploraciones Clínicas'
