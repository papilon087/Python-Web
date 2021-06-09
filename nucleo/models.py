#gustavo
#agustavo20151@gmail.com
#Bardo@123

from django.db import models

from stdimage.models import StdImageField

class Base(models.Model):
    Criacao = models.DateField('Data Criação', auto_now_add=True)
    Modificado = models.DateField('Data de Alteração', auto_now=True)
    Ativo = models.BooleanField('Ativo', default=True)

    class Meta:
        abstract = True


class Servico(Base):
    ICONES_ESCOLHA = (
        ('fa fa-desktop', 'Web Design'),
        ('fa fa-gears', 'Mobile'),
        ('fa fa-rocket', 'Branding'),
        ('fa fa-line-chart', 'Marketing'))
    Nome = models.CharField('Serviço',max_length=100)
    Descricao = models.CharField('Descrição', max_length=200)
    Icone = models.CharField('Icone', max_length=20, choices=ICONES_ESCOLHA)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.Nome


class Cargo(Base):
    Nome = models.CharField('Nome', max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.Nome

class Equipe(Base):
    Nome = models.CharField('Nome', max_length=100)
    Cargo = models.ForeignKey('Cargo', verbose_name='Cargo', on_delete=models.CASCADE)
    Bio = models.CharField('Bio', max_length=200)
    Foto = StdImageField('Foto', upload_to='equipe', variations={'thumbs': {'width': 255, 'height': 255, 'crop': True}})

    class Meta:
        verbose_name = 'Equipe'
        verbose_name_plural = 'Equipes'

    def __str__(self):
        return self.Nome

