from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q, F
from django.http import JsonResponse
from django.views.decorators.http import require_POST, require_http_methods
from django.utils.text import slugify
from .models import Produto, Categoria, PropostaTroca, ProdutoFavorito
from .forms import ProdutoForm

@require_http_methods(["GET"])
def home(request):
    """
    Render the home page with featured products and active categories,
    and handle filtering of products.
    """
    categorias = Categoria.objects.filter(ativa=True)
    
    produtos = Produto.objects.filter(
        status='disponivel'
    ).select_related('usuario', 'categoria', 'marca')
    
    # Apply filters
    categoria_id = request.GET.get('categoria')
    if categoria_id:
        produtos = produtos.filter(categoria_id=categoria_id)
    
    tamanho_fralda = request.GET.get('tamanho_fralda')
    if tamanho_fralda:
        produtos = produtos.filter(tamanho_fralda=tamanho_fralda)
    
    tamanho_roupa = request.GET.get('tamanho_roupa')
    if tamanho_roupa:
        produtos = produtos.filter(tamanho_roupa=tamanho_roupa)
    
    condicao = request.GET.get('condicao')
    if condicao:
        produtos = produtos.filter(condicao=condicao)
    
    busca = request.GET.get('q')
    if busca:
        produtos = produtos.filter(
            Q(titulo__icontains=busca) | 
            Q(descricao__icontains=busca)
        )
    
    ORDENACAO_VALIDA = ['-criado_em', 'criado_em', '-valor_estimado', 'valor_estimado', '-visualizacoes', '-favorito_count']
    ordenacao = request.GET.get('ordenacao', '-criado_em')
    if ordenacao not in ORDENACAO_VALIDA:
        ordenacao = '-criado_em'
    produtos = produtos.order_by(ordenacao)
    
    # For the home page, we might want a smaller limit than the full list
    # Use standardized name 'produtos' for consistent partial usage
    produtos_list = produtos[:12]
    
    filtro_form = ProdutoForm()
    
    context = {
        'categorias_topo': categorias[:6], # Top categories for icons
        'categorias': categorias, # All for filters - standardized name
        'produtos': produtos_list, # Standardized name
        'produto_form': filtro_form,
        'filtros': request.GET.dict(),
    }
    return render(request, 'baby/home.html', context)


@require_http_methods(["GET"])
def lista_produtos(request):
    """
    Render a paginated list of available products with filtering options.
    Filters include category, sizes, condition, and a text search.
    """
    produtos = Produto.objects.filter(
        status='disponivel'
    ).select_related('usuario', 'categoria', 'marca')
    
    categoria_id = request.GET.get('categoria')
    if categoria_id:
        produtos = produtos.filter(categoria_id=categoria_id)
    
    tamanho_fralda = request.GET.get('tamanho_fralda')
    if tamanho_fralda:
        produtos = produtos.filter(tamanho_fralda=tamanho_fralda)
    
    tamanho_roupa = request.GET.get('tamanho_roupa')
    if tamanho_roupa:
        produtos = produtos.filter(tamanho_roupa=tamanho_roupa)
    
    condicao = request.GET.get('condicao')
    if condicao:
        produtos = produtos.filter(condicao=condicao)
    
    busca = request.GET.get('q')
    if busca:
        produtos = produtos.filter(
            Q(titulo__icontains=busca) | 
            Q(descricao__icontains=busca)
        )
    
    ORDENACAO_VALIDA = ['-criado_em', 'criado_em', '-valor_estimado', 'valor_estimado', '-visualizacoes', '-favorito_count']
    ordenacao = request.GET.get('ordenacao', '-criado_em')
    if ordenacao not in ORDENACAO_VALIDA:
        ordenacao = '-criado_em'
    produtos = produtos.order_by(ordenacao)
    
    paginator = Paginator(produtos, 24)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    categorias = Categoria.objects.filter(ativa=True)
    
    filtro_form = ProdutoForm()
    
    context = {
        'page_obj': page_obj,
        'produtos': page_obj.object_list,
        'categorias': categorias,
        'filtros': request.GET.dict(),
        'produto_form': filtro_form,
    }
    return render(request, 'baby/lista_produtos.html', context)


@require_http_methods(["GET"])
def produto_detalhe(request, pk, slug):
    """
    Render the details of a specific product.
    Increments the view count and checks if the authenticated user has favorited it.
    """
    produto = get_object_or_404(
        Produto.objects.select_related('usuario', 'categoria', 'marca'),
        pk=pk
    )
    
    Produto.objects.filter(pk=pk).update(visualizacoes=F('visualizacoes') + 1)
    produto.refresh_from_db()
    
    favoritado = False
    if request.user.is_authenticated:
        favoritado = ProdutoFavorito.objects.filter(
            produto=produto,
            usuario=request.user
        ).exists()
    
    produtos_relacionados = Produto.objects.filter(
        categoria=produto.categoria,
        status='disponivel'
    ).exclude(pk=pk)[:4]
    
    meus_produtos_disponiveis = []
    if request.user.is_authenticated and request.user != produto.usuario:
        meus_produtos_disponiveis = Produto.objects.filter(
            usuario=request.user,
            status='disponivel'
        ).exclude(pk=pk).select_related('categoria')

    context = {
        'produto': produto,
        'favoritado': favoritado,
        'produtos_relacionados': produtos_relacionados,
        'meus_produtos_disponiveis': meus_produtos_disponiveis,
    }
    return render(request, 'baby/produto_detalhe.html', context)


@login_required
@require_http_methods(["GET", "POST"])
def criar_produto(request):
    """
    Handle the creation of a new product listing by an authenticated user.
    """
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            produto = form.save(commit=False)
            produto.usuario = request.user
            produto.save()
            messages.success(request, 'Produto criado com sucesso!')
            return redirect('baby:produto_detalhe', pk=produto.pk, slug=produto.slug)
    else:
        form = ProdutoForm()
    
    return render(request, 'baby/criar_produto.html', {'form': form})


@login_required
@require_http_methods(["GET"])
def meus_produtos(request):
    """
    Render a paginated list of the authenticated user's products.
    """
    produtos_list = Produto.objects.filter(
        usuario=request.user
    ).select_related('categoria').order_by('-criado_em')
    
    paginator = Paginator(produtos_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'baby/meus_produtos.html', {
        'page_obj': page_obj,
        'produtos': page_obj.object_list
    })


@login_required
@require_http_methods(["GET"])
def minhas_trocas(request):
    """
    Render a paginated list of the user's exchange proposals.
    Separates proposals into specific tabs based on perspective (sent/received/history).
    """
    tab = request.GET.get('tab', 'recebidas')
    
    if tab == 'recebidas':
        propostas = PropostaTroca.objects.filter(
            proprietario=request.user
        ).select_related(
            'produto_oferecido', 'produto_desejado', 'proponente'
        ).order_by('-criada_em')
    elif tab == 'enviadas':
        propostas = PropostaTroca.objects.filter(
            proponente=request.user
        ).select_related(
            'produto_oferecido', 'produto_desejado', 'proprietario'
        ).order_by('-criada_em')
    else:
        propostas = PropostaTroca.objects.filter(
            Q(proponente=request.user) | Q(proprietario=request.user),
            status__in=['aceita', 'rejeitada', 'cancelada', 'concluida']
        ).select_related(
            'produto_oferecido', 'produto_desejado'
        ).order_by('-criada_em')
    
    paginator = Paginator(propostas, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'propostas': page_obj.object_list,
        'tab': tab,
    }
    return render(request, 'baby/minhas_trocas.html', context)


@login_required
@require_POST
def criar_proposta(request, produto_id):
    """
    Create a new exchange proposal.
    Validates that the users do not propose trades consisting of their own internal products.
    """
    produto_desejado = get_object_or_404(Produto, pk=produto_id)
    
    if produto_desejado.usuario == request.user:
        messages.error(request, 'Você não pode propor uma troca por um produto que já é seu.')
        return redirect('baby:produto_detalhe', pk=produto_id, slug=produto_desejado.slug)
    
    produto_oferecido_id = request.POST.get('produto_oferecido')
    if not produto_oferecido_id:
        messages.error(request, 'Selecione um produto para oferecer.')
        return redirect('baby:produto_detalhe', pk=produto_id, slug=produto_desejado.slug)
    
    produto_oferecido = get_object_or_404(Produto, pk=produto_oferecido_id, usuario=request.user)
    mensagem = request.POST.get('mensagem', '')
    
    proposta = PropostaTroca.objects.create(
        proponente=request.user,
        proprietario=produto_desejado.usuario,
        produto_oferecido=produto_oferecido,
        produto_desejado=produto_desejado,
        mensagem=mensagem
    )
    
    messages.success(request, 'Proposta enviada com sucesso!')
    return redirect('baby:minhas_trocas')


@login_required
@require_POST
def aceitar_proposta(request, proposta_id):
    """
    Accept an exchange proposal and resolve associated entities.
    Changes internal products' status and automatically rejects competing proposals.
    """
    proposta = get_object_or_404(
        PropostaTroca,
        pk=proposta_id,
        proprietario=request.user,
        status='pendente'
    )
    proposta.aceitar()
    messages.success(request, 'Proposta aceita! Organize a troca com o usuário.')
    return redirect('baby:minhas_trocas')


@login_required
@require_POST
def rejeitar_proposta(request, proposta_id):
    """
    Reject an exchange proposal. Can document a distinct refusal reason.
    """
    proposta = get_object_or_404(
        PropostaTroca,
        pk=proposta_id,
        proprietario=request.user,
        status='pendente'
    )
    motivo = request.POST.get('motivo', '')
    proposta.rejeitar(motivo)
    messages.info(request, 'Proposta rejeitada.')
    return redirect('baby:minhas_trocas')


@login_required
@require_POST
def favoritar_produto(request):
    """
    Toggle a product's beloved (favorite) status for the currently authenticated user.
    Called via Ajax.
    """
    produto_id = request.POST.get('produto_id')
    produto = get_object_or_404(Produto, pk=produto_id)
    
    favorito, created = ProdutoFavorito.objects.get_or_create(
        produto=produto,
        usuario=request.user
    )
    
    if not created:
        favorito.delete()
        favoritado = False
        Produto.objects.filter(pk=produto_id).update(
            favorito_count=F('favorito_count') - 1
        )
    else:
        favoritado = True
        Produto.objects.filter(pk=produto_id).update(
            favorito_count=F('favorito_count') + 1
        )
    
    produto.refresh_from_db()
    return JsonResponse({'favoritado': favoritado, 'count': produto.favorito_count})


@login_required
@require_http_methods(["GET"])
def meus_favoritos(request):
    """
    Render a paginated lineup of the authenticated user's favorite products.
    """
    favoritos_list = ProdutoFavorito.objects.filter(
        usuario=request.user
    ).select_related('produto__categoria').order_by('-criado_em')
    
    paginator = Paginator(favoritos_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'baby/meus_favoritos.html', {
        'page_obj': page_obj,
        'favoritos': page_obj.object_list
    })


@require_http_methods(["GET"])
def categoria_view(request, slug):
    """
    Render a paginated list of available products filtered by a specific category.
    """
    categoria = get_object_or_404(Categoria, slug=slug, ativa=True)
    produtos = Produto.objects.filter(
        categoria=categoria,
        status='disponivel'
    ).select_related('usuario', 'categoria').order_by('-criado_em')
    
    paginator = Paginator(produtos, 24)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'categoria': categoria,
        'page_obj': page_obj,
        'produtos': page_obj.object_list,
    }
    return render(request, 'baby/categoria.html', context)
