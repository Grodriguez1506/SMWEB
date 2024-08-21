# Generated by Django 5.0.4 on 2024-08-20 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SMWEB', '0008_affiliation'),
    ]

    operations = [
        migrations.AddField(
            model_name='affiliation',
            name='affiliation_cost',
            field=models.DecimalField(decimal_places=2, default=96700.0, max_digits=20, null=True, verbose_name='Costo de afiliación'),
        ),
    ]
