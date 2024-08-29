# Generated by Django 5.0.4 on 2024-08-20 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SMWEB', '0011_rejectedaffiliation'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApprovedAffiliation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=255, verbose_name='Número de caso')),
                ('client', models.CharField(default='', max_length=255, verbose_name='Cliente')),
                ('city', models.CharField(max_length=255, verbose_name='Ciudad')),
                ('in_charge', models.CharField(default='', max_length=255, verbose_name='Encargado')),
                ('full_name', models.CharField(max_length=255, verbose_name='Nombres y Apellidos')),
                ('since', models.DateField(verbose_name='Desde')),
                ('up_to', models.DateField(verbose_name='Hasta')),
                ('company', models.CharField(max_length=255, verbose_name='Empresa')),
                ('created_by', models.CharField(max_length=255, verbose_name='Realizado por')),
                ('created_at', models.DateField(verbose_name='Realizado el')),
                ('affiliation_cost', models.DecimalField(decimal_places=2, default=96700.0, max_digits=20, verbose_name='Costo de afiliación')),
                ('approved_at', models.DateField(auto_now_add=True, verbose_name='Aprobado el')),
                ('approved_by', models.CharField(max_length=255, verbose_name='Aprobado por')),
            ],
            options={
                'verbose_name': 'Afiliación aprobada',
                'verbose_name_plural': 'Afiliaiciones aprobadas',
            },
        ),
    ]