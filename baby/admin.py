from django.contrib import admin
from .models import Categoria, Marca, Produto, PropostaTroca, Mensagem, ProdutoFavorito


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'slug', 'ordem', 'ativa']
    list_filter = ['ativa']
    prepopulated_fields = {'slug': ('nome',)}
    ordering = ['ordem', 'nome']
    search_fields = ['nome']


@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'slug']
    prepopulated_fields = {'slug': ('nome',)}
    search_fields = ['nome']


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'usuario', 'categoria', 'status', 'condicao', 'criado_em']
    list_filter = ['status', 'categoria', 'condicao', 'criado_em']
    search_fields = ['titulo', 'descricao']
    readonly_fields = ['visualizacoes', 'favorito_count', 'criado_em', 'atualizado_em']
    date_hierarchy = 'criado_em'
    raw_id_fields = ['usuario']
    ordering = ['-criado_em']


@admin.register(PropostaTroca)
class PropostaTrocaAdmin(admin.ModelAdmin):
    list_display = ['id', 'proponente', 'proprietario', 'status', 'criada_em']
    list_filter = ['status', 'criada_em']
    search_fields = ['proponente__email', 'proprietario__email']
    date_hierarchy = 'criada_em'
    readonly_fields = ['id', 'criada_em', 'atualizada_em']


@admin.register(Mensagem)
class MensagemAdmin(admin.ModelAdmin):
    list_display = ['remetente', 'destinatario', 'lida', 'criada_em']
    list_filter = ['lida', 'criada_em']
    search_fields = ['remetente__email', 'destinatario__email', 'conteudo']
    date_hierarchy = 'criada_em'


@admin.register(ProdutoFavorito)
class ProdutoFavoritoAdmin(admin.ModelAdmin):
    list_display = ['produto', 'usuario', 'criado_em']
    list_filter = ['criado_em']
    search_fields = ['produto__titulo', 'usuario__email']
    date_hierarchy = 'criado_em'
