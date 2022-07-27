# Generated by Django 4.0.6 on 2022-07-27 01:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda_PQRS_app', '0008_alter_pqrs_identification_number_alter_pqrs_num_cell_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pqrs',
            name='num_cell',
            field=models.CharField(blank=True, max_length=16, null=True, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{10,13}$')]),
        ),
        migrations.AlterField(
            model_name='pqrs',
            name='num_house',
            field=models.CharField(blank=True, max_length=16, null=True, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{7,10}$')]),
        ),
    ]
