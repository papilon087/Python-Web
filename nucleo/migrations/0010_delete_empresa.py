# Generated by Django 3.2.3 on 2021-06-02 01:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nucleo', '0009_remove_empresa_descricao'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Empresa',
        ),
    ]
