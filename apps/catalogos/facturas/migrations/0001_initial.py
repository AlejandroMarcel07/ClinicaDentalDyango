# Generated by Django 4.2 on 2024-10-02 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TbFactura',
            fields=[
                ('idfactura', models.AutoField(db_column='IdFactura', primary_key=True, serialize=False)),
                ('costototal', models.DecimalField(db_column='CostoTotal', decimal_places=0, max_digits=18)),
                ('tipopago', models.CharField(db_collation='Modern_Spanish_CI_AS', db_column='TipoPago', max_length=50)),
                ('descuentoaplicado', models.BooleanField(db_column='DescuentoAplicado')),
                ('montodescuento', models.DecimalField(blank=True, db_column='MontoDescuento', decimal_places=0, max_digits=18, null=True)),
                ('pagounico', models.BooleanField(db_column='PagoUnico')),
                ('cantidadcuotas', models.IntegerField(blank=True, db_column='CantidadCuotas', null=True)),
                ('cuotaspagadas', models.IntegerField(blank=True, db_column='CuotasPagadas', null=True)),
                ('costoporcuota', models.DecimalField(blank=True, db_column='CostoPorCuota', decimal_places=0, max_digits=18, null=True)),
                ('cancelado', models.BooleanField(db_column='Cancelado')),
                ('totaldescuentoaplicado', models.DecimalField(blank=True, db_column='TotalDescuentoAplicado', decimal_places=0, max_digits=18, null=True)),
            ],
            options={
                'verbose_name': 'Factura',
                'verbose_name_plural': 'Facturas',
                'db_table': 'Tb_Factura',
                'managed': False,
            },
        ),
    ]
