# Generated by Django 5.0.4 on 2024-09-08 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SMWEB', '0012_approvedaffiliation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderpayment',
            name='comments',
            field=models.TextField(default=' ', verbose_name='Comentarios'),
        ),
    ]