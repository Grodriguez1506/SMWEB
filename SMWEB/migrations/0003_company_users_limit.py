# Generated by Django 5.0.4 on 2024-08-04 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SMWEB', '0002_company_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='users_limit',
            field=models.IntegerField(default=10, verbose_name='Limite de usuarios'),
        ),
    ]
