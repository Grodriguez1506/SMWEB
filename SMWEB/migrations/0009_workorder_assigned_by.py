# Generated by Django 5.0.4 on 2024-08-04 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SMWEB', '0008_workorder_in_charge'),
    ]

    operations = [
        migrations.AddField(
            model_name='workorder',
            name='assigned_by',
            field=models.CharField(default='', max_length=255, verbose_name='Asignado por'),
        ),
    ]
