# Generated by Django 5.0.4 on 2024-08-02 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SMWEB', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='status',
            field=models.BooleanField(default=True, verbose_name='¿Activo?'),
        ),
    ]
