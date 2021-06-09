# Generated by Django 3.2.3 on 2021-05-26 23:48

from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('nucleo', '0003_delete_portifolio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portifolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Criacao', models.DateField(auto_now_add=True, verbose_name='Data Criação')),
                ('Modificado', models.DateField(auto_now=True, verbose_name='Data de Alteração')),
                ('Ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('Nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('Imagem', stdimage.models.StdImageField(upload_to='equipe', verbose_name='Foto')),
            ],
            options={
                'verbose_name': 'Portifólio',
                'verbose_name_plural': 'Portifólios',
            },
        ),
    ]
