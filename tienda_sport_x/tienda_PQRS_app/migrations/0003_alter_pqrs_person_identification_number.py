# Generated by Django 4.0.6 on 2022-07-26 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda_PQRS_app', '0002_alter_pqrs_person_options_alter_pqrs_tiket_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pqrs_person',
            name='identification_number',
            field=models.IntegerField(unique=True),
        ),
    ]
