# Generated by Django 4.2 on 2024-10-02 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TbGenero',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('genero', models.CharField(db_collation='Modern_Spanish_CI_AS', db_column='Genero', max_length=9)),
            ],
            options={
                'verbose_name': 'Genero',
                'verbose_name_plural': 'Generos',
                'db_table': 'Tb_Genero',
                'managed': False,
            },
        ),
    ]
