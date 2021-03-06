# Generated by Django 3.2.3 on 2021-06-09 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nucleo', '0020_social'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Criacao', models.DateField(auto_now_add=True, verbose_name='Data Criação')),
                ('Modificado', models.DateField(auto_now=True, verbose_name='Data de Alteração')),
                ('Ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('Nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('Descricao', models.CharField(max_length=200, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'About',
                'verbose_name_plural': 'Abouts',
            },
        ),
        migrations.DeleteModel(
            name='Social',
        ),
    ]
