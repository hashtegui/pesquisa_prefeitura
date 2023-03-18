from django.contrib import admin

from pesquisa.models import CustomUser


# Register your models here.

@admin.register(CustomUser)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'cpf')
