# Generated by Django 3.2.3 on 2021-06-02 01:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nucleo', '0008_empresa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empresa',
            name='Descricao',
        ),
    ]
