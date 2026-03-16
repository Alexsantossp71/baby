import uuid
from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError


def validar_tamanho_imagem(file):
    """Valida que a imagem não exceda 5MB."""
    limite_mb = 5
    if file.size > limite_mb * 1024 * 1024:
        raise ValidationError(f'O arquivo não pode exceder {limite_mb}MB. Tamanho atual: {file.size / (1024*1024):.1f}MB')

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    icone = models.CharField(max_length=50, blank=True)
    descricao = models.TextField(blank=True)
    ordem = models.PositiveIntegerField(default=0)
    ativa = models.BooleanField(default=True)
    cor = models.CharField(max_length=7, default='#ec5b13')

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['ordem', 'nome']

    def __str__(self):
        return self.nome


class Marca(models.Model):
    nome = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    logo = models.ImageField(upload_to='marcas/', blank=True)

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Produto(models.Model):
    TAMANHO_FRALDA_CHOICES = [
        ('rn', 'RN'), ('p', 'P'), ('m', 'M'), ('g', 'G'), ('gg', 'GG'), ('xg', 'XG')
    ]
    
    TAMANHO_ROUPA_CHOICES = [
        ('rn', 'RN'), ('0_3m', '0-3m'), ('3_6m', '3-6m'), ('6_9m', '6-9m'), 
        ('9_12m', '9-12m'), ('12_18m', '12-18m'), ('18_24m', '18-24m'), 
        ('2t', '2 anos'), ('3t', '3 anos'), ('4t', '4 anos'), ('5t', '5 anos')
    ]
    
    GENERO_CHOICES = [
        ('masculino', 'Masculino'), ('feminino', 'Feminino'), ('unisex', 'Unisex')
    ]
    
    CONDICAO_CHOICES = [
        ('novo', 'Novo'), ('seminovo', 'Seminovo'), 
        ('usado_otimo', 'Usado - Ótimo'), ('usado_bom', 'Usado - Bom'), 
        ('usado_regular', 'Usado - Regular')
    ]
    
    STATUS_CHOICES = [
        ('disponivel', 'Disponível'), ('reservado', 'Reservado'), 
        ('em_troca', 'Em Troca'), ('trocado', 'Trocado'), ('indisponivel', 'Indisponível')
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, blank=True)
    descricao = models.TextField()
    tamanho_fralda = models.CharField(max_length=10, choices=TAMANHO_FRALDA_CHOICES, null=True, blank=True)
    tamanho_roupa = models.CharField(max_length=10, choices=TAMANHO_ROUPA_CHOICES, null=True, blank=True)
    cor = models.CharField(max_length=50, blank=True)
    para_bebe = models.BooleanField(default=True)
    para_mae = models.BooleanField(default=False)
    genero = models.CharField(max_length=20, choices=GENERO_CHOICES, default='unisex')
    condicao = models.CharField(max_length=20, choices=CONDICAO_CHOICES, default='seminovo')
    valor_estimado = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    aceita_troca = models.BooleanField(default=True)
    preferencias_troca = models.TextField(blank=True)
    
    _image_validators = [
        FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'webp', 'gif']),
        validar_tamanho_imagem,
    ]
    
    imagem_principal = models.ImageField(upload_to='produtos/', validators=_image_validators)
    imagem_2 = models.ImageField(upload_to='produtos/', null=True, blank=True, validators=_image_validators)
    imagem_3 = models.ImageField(upload_to='produtos/', null=True, blank=True, validators=_image_validators)
    imagem_4 = models.ImageField(upload_to='produtos/', null=True, blank=True, validators=_image_validators)
    imagem_5 = models.ImageField(upload_to='produtos/', null=True, blank=True, validators=_image_validators)
    
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    bairro = models.CharField(max_length=100, blank=True)
    mostrar_localizacao = models.BooleanField(default=False)
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='disponivel')
    visualizacoes = models.PositiveIntegerField(default=0)
    favorito_count = models.PositiveIntegerField(default=0)
    
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, related_name='produtos')
    marca = models.ForeignKey(Marca, on_delete=models.SET_NULL, null=True, blank=True, related_name='produtos')
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='produtos')

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['-criado_em']
        indexes = [
            models.Index(fields=['status', 'criado_em'], name='baby_produt_status_31ce0a_idx'),
            models.Index(fields=['categoria', 'status'], name='baby_produt_categor_40e6ce_idx'),
        ]

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titulo) or str(self.id)[:8]
        super().save(*args, **kwargs)


class PropostaTroca(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('aceita', 'Aceita'),
        ('rejeitada', 'Rejeitada'),
        ('cancelada', 'Cancelada'),
        ('concluida', 'Concluída')
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    mensagem = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')
    motivo_recusa = models.TextField(blank=True)
    criada_em = models.DateTimeField(auto_now_add=True)
    atualizada_em = models.DateTimeField(auto_now=True)
    
    produto_desejado = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='propostas_como_desejo')
    produto_oferecido = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='propostas_como_oferta')
    proponente = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='propostas_feitas')
    proprietario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='propostas_recebidas')

    class Meta:
        verbose_name = 'Proposta de Troca'
        verbose_name_plural = 'Propostas de Troca'
        ordering = ['-criada_em']

    def __str__(self):
        return f"Proposta para {self.produto_desejado.titulo}"

    def aceitar(self):
        self.status = 'aceita'
        self.save()
        
        self.produto_oferecido.status = 'trocado'
        self.produto_oferecido.save()
        
        self.produto_desejado.status = 'trocado'
        self.produto_desejado.save()
        
        propostas_pendentes = PropostaTroca.objects.filter(
            models.Q(produto_desejado__in=[self.produto_oferecido, self.produto_desejado]) |
            models.Q(produto_oferecido__in=[self.produto_oferecido, self.produto_desejado]),
            status='pendente'
        ).exclude(id=self.id)
        
        for p in propostas_pendentes:
            p.rejeitar('Um dos produtos envolvidos na troca não está mais disponível.')

    def rejeitar(self, motivo=''):
        self.status = 'rejeitada'
        if motivo:
            self.motivo_recusa = motivo
        self.save()


class Mensagem(models.Model):
    conteudo = models.TextField()
    lida = models.BooleanField(default=False)
    criada_em = models.DateTimeField(auto_now_add=True)
    
    destinatario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='mensagens_recebidas')
    remetente = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='mensagens_enviadas')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Mensagem'
        verbose_name_plural = 'Mensagens'
        ordering = ['-criada_em']

    def __str__(self):
        return f"Mensagem de {self.remetente} para {self.destinatario}"


class ProdutoFavorito(models.Model):
    criado_em = models.DateTimeField(auto_now_add=True)
    
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='favoritos')
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='favoritos')

    class Meta:
        unique_together = ('produto', 'usuario')

    def __str__(self):
        return f"{self.produto.titulo} favoritado por {self.usuario}"
