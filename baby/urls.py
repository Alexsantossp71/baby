from django.urls import path
from . import views

app_name = 'baby'

urlpatterns = [
    path('', views.home, name='home'),
    path('produtos/', views.lista_produtos, name='lista_produtos'),
    path('produto/<uuid:pk>/<slug:slug>/', views.produto_detalhe, name='produto_detalhe'),
    path('anunciar/', views.criar_produto, name='criar_produto'),
    path('meus-produtos/', views.meus_produtos, name='meus_produtos'),
    path('trocas/', views.minhas_trocas, name='minhas_trocas'),
    path('troca/<uuid:proposta_id>/aceitar/', views.aceitar_proposta, name='aceitar_proposta'),
    path('troca/<uuid:proposta_id>/rejeitar/', views.rejeitar_proposta, name='rejeitar_proposta'),
    path('troca/<uuid:produto_id>/propor/', views.criar_proposta, name='criar_proposta'),
    path('favoritar/', views.favoritar_produto, name='favoritar_produto'),
    path('favoritos/', views.meus_favoritos, name='meus_favoritos'),
    path('categoria/<str:slug>/', views.categoria_view, name='categoria'),
    path('produto/<uuid:pk>/excluir/', views.excluir_produto, name='excluir_produto'),
]
