# Generated by Django 4.2 on 2024-10-02 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TbRecetamedica',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('descripcion', models.TextField(blank=True, db_collation='Modern_Spanish_CI_AS', db_column='Descripcion', null=True)),
            ],
            options={
                'verbose_name': 'Receta Medica',
                'verbose_name_plural': 'Recetas Medicas',
                'db_table': 'Tb_RecetaMedica',
                'managed': False,
            },
        ),
    ]
