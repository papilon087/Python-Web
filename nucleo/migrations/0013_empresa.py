# Generated by Django 3.2.3 on 2021-06-02 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nucleo', '0012_delete_empresa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Criacao', models.DateField(auto_now_add=True, verbose_name='Data Criação')),
                ('Modificado', models.DateField(auto_now=True, verbose_name='Data de Alteração')),
                ('Ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('Nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('Bio', models.CharField(max_length=200, verbose_name='Bio')),
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresas',
            },
        ),
    ]