from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ['email', 'username', 'first_name', 'last_name', 'tipo_usuario', 'is_verified', 'is_active', 'data_cadastro']
    list_filter = ['tipo_usuario', 'is_verified', 'is_active', 'is_staff', 'data_cadastro']
    search_fields = ['email', 'username', 'first_name', 'last_name', 'cidade', 'estado']
    ordering = ['-data_cadastro']
    
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Informações Adicionais', {
            'fields': ('tipo_usuario', 'telefone', 'foto', 'bio', 'cidade', 'estado', 'data_nascimento', 'possui_filhos', 'filhos_count', 'receber_notificacoes', 'is_verified', 'facebook', 'instagram')
        }),
    )
    
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ('Informações Adicionais', {
            'fields': ('tipo_usuario', 'telefone', 'cidade', 'estado')
        }),
    )
