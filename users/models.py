from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Modelo de usuário personalizado"""
    
    TIPO_USUARIO_CHOICES = [
        ('geral', 'Permuta Geral'),
        ('baby', 'Permutas Baby'),
        ('ambos', 'Ambos'),
    ]
    
    email = models.EmailField(unique=True, verbose_name='Email')
    tipo_usuario = models.CharField(
        max_length=10, 
        choices=TIPO_USUARIO_CHOICES, 
        default='baby',
        verbose_name='Tipo de Usuário'
    )
    telefone = models.CharField(max_length=20, blank=True, verbose_name='Telefone')
    foto = models.ImageField(upload_to='perfis/', blank=True, null=True, verbose_name='Foto')
    bio = models.TextField(blank=True, verbose_name='Biografia')
    cidade = models.CharField(max_length=100, blank=True, verbose_name='Cidade')
    estado = models.CharField(max_length=2, blank=True, verbose_name='Estado')
    data_nascimento = models.DateField(null=True, blank=True, verbose_name='Data de Nascimento')
    possui_filhos = models.BooleanField(default=False, verbose_name='Possui Filhos')
    filhos_count = models.PositiveIntegerField(default=0, verbose_name='Quantidade de Filhos')
    receber_notificacoes = models.BooleanField(default=True, verbose_name='Receber Notificações')
    data_cadastro = models.DateTimeField(auto_now_add=True, verbose_name='Data de Cadastro')
    ultimo_acesso = models.DateTimeField(auto_now=True, verbose_name='Último Acesso')
    is_verified = models.BooleanField(default=False, verbose_name='Verificado')
    facebook = models.CharField(max_length=100, blank=True, verbose_name='Facebook')
    instagram = models.CharField(max_length=100, blank=True, verbose_name='Instagram')
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    class Meta:
        db_table = 'users'
        ordering = ['-data_cadastro']
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
    
    def __str__(self):
        return self.email
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}".strip() or self.username
    
    def get_initials(self):
        if self.first_name and self.last_name:
            return f"{self.first_name[0]}{self.last_name[0]}".upper()
        return self.username[0].upper()
