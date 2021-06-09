from django.contrib import admin

from .models import Servico, Cargo, Equipe

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('Nome', 'Icone', 'Ativo', 'Modificado')

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('Nome', 'Ativo', 'Modificado')

@admin.register(Equipe)
class EquipeAdmin(admin.ModelAdmin):
    list_display = ('Nome', 'Cargo', 'Ativo', 'Modificado')









