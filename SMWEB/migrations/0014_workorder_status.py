# Generated by Django 5.0.4 on 2024-08-06 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SMWEB', '0013_workorder'),
    ]

    operations = [
        migrations.AddField(
            model_name='workorder',
            name='status',
            field=models.CharField(default='Activo', max_length=50, verbose_name='Estado'),
        ),
    ]
