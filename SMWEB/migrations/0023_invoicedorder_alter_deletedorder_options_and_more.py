# Generated by Django 5.0.4 on 2024-08-11 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SMWEB', '0022_deletedorder'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvoicedOrder',
            fields=[
                ('order_id', models.CharField(max_length=255, primary_key=True, serialize=False, verbose_name='Número de caso')),
                ('client', models.CharField(default='', max_length=255, verbose_name='Cliente')),
                ('city', models.CharField(max_length=255, verbose_name='Ciudad')),
                ('invesment', models.DecimalField(decimal_places=2, max_digits=20, null=True, verbose_name='Inversión')),
                ('sales_value', models.DecimalField(decimal_places=2, max_digits=20, null=True, verbose_name='Valor de venta')),
                ('service_description', models.TextField(verbose_name='Descripción del servicio')),
                ('remarks', models.TextField(null=True, verbose_name='Observaciones del caso')),
                ('in_charge', models.CharField(default='', max_length=255, verbose_name='Encargado')),
                ('assigned_by', models.CharField(default='', max_length=255, verbose_name='Asignado por')),
                ('status', models.CharField(default='Activo', max_length=50, verbose_name='Estado')),
                ('company', models.CharField(default='', max_length=255, verbose_name='Empresa')),
                ('invoiced_by', models.CharField(default='', max_length=255, verbose_name='facturado por')),
                ('invoice_id', models.CharField(default='', max_length=255, verbose_name='Número de factura')),
                ('invoiced_at', models.DateField(auto_now_add=True, verbose_name='Fecha de factura')),
            ],
            options={
                'verbose_name': 'Orden facturada',
                'verbose_name_plural': 'Ordenes facturadas',
            },
        ),
        migrations.AlterModelOptions(
            name='deletedorder',
            options={'verbose_name': 'Orden eliminada', 'verbose_name_plural': 'Ordenes eliminadas'},
        ),
        migrations.AlterModelOptions(
            name='finishedorder',
            options={'verbose_name': 'Orden finalizada', 'verbose_name_plural': 'Ordenes finalizadas'},
        ),
    ]
