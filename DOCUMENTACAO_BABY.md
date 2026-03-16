# Documentação do Projeto: Permutas Baby

Este documento consolida as informações essenciais para o uso, teste e entrega do projeto **Permutas Baby**, desenvolvido como parte da disciplina de Programação para Internet.

## 1. Visão Geral
O **Permutas Baby** é uma plataforma de troca de produtos infantis e para gestantes. O objetivo é facilitar a economia circular entre famílias, permitindo que itens que não servem mais para uma criança possam ser trocados por outros de interesse.

## 2. Funcionalidades Principais
- **Catálogo de Produtos:** Listagem dinâmica com filtros por categoria, tamanho (fraldas e roupas), condição e busca textual.
- **Gestão de Produtos:** Cadastro de itens com múltiplas imagens e controle de status (Disponível, Reservado, Trocado).
- **Sistema de Trocas:** Fluxo completo de proposta, aceitação e rejeição de trocas entre usuários.
- **Favoritos:** Possibilidade de salvar produtos de interesse para acompanhamento.
- **Dashboard do Usuário:** Áreas específicas para gerenciar "Meus Produtos", "Minhas Trocas" e "Meus Favoritos".

## 3. Modelos de Dados (App: `baby`)
- **Categoria:** Organiza os produtos (ex: Fraldas, Roupas, Brinquedos).
- **Marca:** Identifica fabricantes dos itens.
- **Produto:** Modelo central contendo detalhes técnicos, imagens, localização e status.
- **PropostaTroca:** Gerencia a interação entre o proponente e o proprietário, vinculando os itens envolvidos.
- **ProdutoFavorito:** Relação Many-to-Many simplificada para gerenciar itens favoritados.

## 4. Endpoints Principais (URLs)
| Endpoint | Nome | Descrição |
|----------|------|-----------|
| `/baby/` | `home` | Página inicial com destaques e filtros rápidos. |
| `/baby/produtos/` | `lista_produtos` | Listagem completa e paginada. |
| `/baby/produto/criar/` | `criar_produto` | Formulário de anúncio de novo item. |
| `/baby/trocas/` | `minhas_trocas` | Central de propostas enviadas e recebidas. |
| `/baby/favoritos/` | `meus_favoritos` | Itens marcados como favoritos. |

## 5. Credenciais de Teste
Para validar as funcionalidades sem criar novas contas, utilize os usuários pré-cadastrados:

| Username | Senha | Observação |
|----------|-------|------------|
| `joao_silva` | `senha123` | Possui produtos e propostas pendentes. |
| `maria_santos` | `senha123` | Ideal para testar o recebimento de propostas. |
| `pedro_oliveira`| `senha123` | Usuário com itens variados. |

**URL de Login:** `http://127.0.0.1:8000/accounts/login/`

## 6. Guia de Execução Local
1. Certifique-se de ter as dependências instaladas: `pip install -r requirements.txt`
2. Execute as migrações: `python manage.py migrate`
3. Inicie o servidor: `python manage.py runserver`

## 7. Deploy (PythonAnywhere)
O projeto está configurado para deploy no servidor PythonAnywhere.
- **Host:** `PI2016G4.pythonanywhere.com`
- **Configuração WSGI:** Aponta para `permutas_site.settings`.
- **Arquivos Estáticos:** Gerenciados via WhiteNoise e configurados na aba 'Web' do painel PA.

---
*Documento gerado automaticamente para entrega do projeto PI-2016.*
