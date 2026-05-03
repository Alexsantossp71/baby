# Anexo: Templates HTML (Frontend) - Projeto Baby Lake

Este anexo contém a íntegra dos arquivos de template (HTML/Django Template Language) que compõem a interface do usuário da plataforma Baby Lake. Os templates utilizam o framework Tailwind CSS para estilização e DTL para lógica de renderização dinâmica.

---

## 1. Templates de Estrutura (Base)

### 1.1 templates/base.html
*Template base global que define o esqueleto de todas as páginas do site (Header, Footer e Meta Tags).*

```html
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Permutas - Troque produtos com pessoas próximas{% endblock %}</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary: #10b981;
            --primary-dark: #059669;
            --primary-light: #d1fae5;
            --secondary: #1e293b;
            --accent: #f59e0b;
            --danger: #ef4444;
            --gray-50: #f9fafb;
            --gray-100: #f3f4f6;
            --gray-200: #e5e7eb;
            --gray-300: #d1d5db;
            --gray-400: #9ca3af;
            --gray-500: #6b7280;
            --gray-600: #4b5563;
            --gray-700: #374151;
            --gray-800: #1f2937;
            --gray-900: #111827;
            --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
            --shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px 0 rgba(0, 0, 0, 0.06);
            --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
            --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
            --shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Poppins', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            line-height: 1.6;
            color: var(--gray-800);
            background: var(--gray-50);
        }

        a {
            text-decoration: none;
            color: inherit;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 1.5rem;
        }

        header {
            background: white;
            box-shadow: var(--shadow-sm);
            position: sticky;
            top: 0;
            z-index: 100;
        }

        .navbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 1rem 0;
        }

        .logo {
            font-size: 1.5rem;
            font-weight: 700;
            color: var(--primary);
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        .logo-icon {
            width: 36px;
            height: 36px;
            background: linear-gradient(135deg, var(--primary) 0%, var(--primary-dark) 100%);
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-weight: bold;
            font-size: 1.2rem;
        }

        .nav-links {
            display: flex;
            align-items: center;
            gap: 2rem;
        }

        .nav-links a {
            color: var(--gray-600);
            font-weight: 500;
            transition: color 0.2s;
            font-size: 0.95rem;
        }

        .nav-links a:hover {
            color: var(--primary);
        }

        .nav-actions {
            display: flex;
            align-items: center;
            gap: 0.75rem;
        }

        .btn {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            padding: 0.625rem 1.25rem;
            font-weight: 500;
            border-radius: 10px;
            border: none;
            cursor: pointer;
            transition: all 0.2s;
            font-size: 0.95rem;
            font-family: inherit;
        }

        .btn-ghost {
            background: transparent;
            color: var(--gray-600);
        }

        .btn-ghost:hover {
            background: var(--gray-100);
            color: var(--gray-900);
        }

        .btn-primary {
            background: linear-gradient(135deg, var(--primary) 0%, var(--primary-dark) 100%);
            color: white;
            box-shadow: 0 2px 4px rgba(16, 185, 129, 0.3);
        }

        .btn-primary:hover {
            transform: translateY(-1px);
            box-shadow: 0 4px 8px rgba(16, 185, 129, 0.4);
        }

        .btn-outline {
            background: transparent;
            border: 2px solid var(--gray-300);
            color: var(--gray-700);
        }

        .btn-outline:hover {
            border-color: var(--primary);
            color: var(--primary);
        }

        .btn-success {
            background: var(--primary);
            color: white;
        }

        .btn-success:hover {
            background: var(--primary-dark);
        }

        .btn-danger {
            background: var(--danger);
            color: white;
        }

        .btn-danger:hover {
            background: #dc2626;
        }

        .btn-sm {
            padding: 0.375rem 0.75rem;
            font-size: 0.85rem;
        }

        main {
            min-height: calc(100vh - 200px);
        }

        .footer-grid {
            display: grid;
            grid-template-columns: 2fr 1fr 1fr 1fr;
            gap: 3rem;
            margin-bottom: 3rem;
        }

        footer {
            background: var(--secondary);
            color: white;
            padding: 4rem 0 2rem;
        }

        .footer-bottom {
            border-top: 1px solid var(--gray-700);
            padding-top: 1.5rem;
            text-align: center;
            color: var(--gray-500);
            font-size: 0.875rem;
        }

        .messages {
            list-style: none;
            padding: 0;
            margin-bottom: 1.5rem;
        }

        .messages li {
            padding: 1rem 1.25rem;
            margin-bottom: 0.75rem;
            border-radius: 12px;
            font-weight: 500;
        }

        .messages .success {
            background: linear-gradient(135deg, var(--primary-light) 0%, #ecfdf5 100%);
            color: var(--primary-dark);
            border-left: 4px solid var(--primary);
        }

        .messages .error {
            background: linear-gradient(135deg, #fee2e2 0%, #fef2f2 100%);
            color: #991b1b;
            border-left: 4px solid var(--danger);
        }
    </style>
    {% block extra_css %}{% endblock %}
</head>
<body>
    <header>
        <div class="container">
            <nav class="navbar">
                <a href="{% url 'baby:home' %}" class="logo">
                    <div class="logo-icon">P</div>
                    Permutas Baby
                </a>
                
                <div class="nav-links">
                    <a href="{% url 'baby:home' %}">Início</a>
                    <a href="{% url 'sobre' %}#como-funciona">Como Funciona</a>
                    <a href="#recursos">Recursos</a>
                </div>
                
                <div class="nav-actions">
                    {% if user.is_authenticated %}
                        <a href="{% url 'baby:criar_produto' %}" class="btn btn-primary">
                            + Anunciar
                        </a>
                        <a href="{% url 'baby:minhas_trocas' %}" class="btn btn-ghost">Minhas Trocas</a>
                        <a href="{% url 'users:perfil' %}" style="color: var(--gray-500); font-size: 0.9rem; transition: all 0.2s; text-decoration: none; padding: 0.5rem 0.75rem; border-radius: 8px;" 
                           onmouseover="this.style.color='var(--primary)'; this.style.background='var(--primary-light)';"
                           onmouseout="this.style.color='var(--gray-500)'; this.style.background='transparent';">
                            {{ user.username }}
                        </a>
                        <form method="post" action="{% url 'users:logout' %}" style="display: inline;">{% csrf_token %}<button type="submit" class="btn btn-ghost" style="color: var(--gray-400); font-size: 0.85rem;">Sair</button></form>
                    {% else %}
                        <a href="{% url 'users:login' %}" class="btn btn-ghost">Entrar</a>
                        <a href="{% url 'users:register' %}" class="btn btn-primary">Criar Conta</a>
                    {% endif %}
                </div>
            </nav>
        </div>
    </header>

    {% block hero %}{% endblock %}

    <main>
        <div class="container">
            {% if messages %}
                <ul class="messages">
                    {% for message in messages %}
                        <li class="{{ message.tags }}">{{ message }}</li>
                    {% endfor %}
                </ul>
            {% endif %}
            
            {% block content %}{% endblock %}
        </div>
    </main>

    <footer>
        <div class="container">
            <div class="footer-grid">
                <div class="footer-brand">
                    <a href="{% url 'baby:home' %}" class="logo">
                        <div class="logo-icon">P</div>
                        Permutas Baby
                    </a>
                    <p>Troque produtos com pessoas próximas de você. Simples, gratuito e sustentável. A nova forma de consumir de forma consciente.</p>
                </div>
                
                <div>
                    <h4 class="footer-title">Navegação</h4>
                    <ul class="footer-links">
                        <li><a href="{% url 'baby:home' %}">Página Inicial</a></li>
                        <li><a href="{% url 'baby:criar_produto' %}">Anunciar</a></li>
                        <li><a href="{% url 'users:login' %}">Entrar</a></li>
                        <li><a href="{% url 'users:register' %}">Criar Conta</a></li>
                    </ul>
                </div>
                
                <div>
                    <h4 class="footer-title">Categorias</h4>
                    <ul class="footer-links">
                        <li><a href="?categoria=1">Eletrônicos</a></li>
                        <li><a href="?categoria=2">Roupas</a></li>
                        <li><a href="?categoria=3">Livros</a></li>
                        <li><a href="?categoria=4">Móveis</a></li>
                    </ul>
                </div>
                
                <div>
                    <h4 class="footer-title">Legal</h4>
                    <ul class="footer-links">
                        <li><a href="#">Termos de Uso</a></li>
                        <li><a href="#">Política de Privacidade</a></li>
                        <li><a href="#">Contato</a></li>
                    </ul>
                </div>
            </div>
            
            <div class="footer-bottom">
                <p>&copy; 2026 Permutas. Projetoopencode sem fins lucrativos. Feito com 💚 para conectar pessoas.</p>
            </div>
        </div>
    </footer>
</body>
</html>
```

### 1.2 templates/baby/base_baby.html
*Template base específico do aplicativo Baby Lake, utilizando Tailwind CSS moderno e ícones Material Symbols.*

```html
<!DOCTYPE html>
<html class="light" lang="pt-BR">
<head>
    <meta charset="utf-8"/>
    <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
    <title>{% block title %}Permutas Baby{% endblock %}</title>
    <script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
    <link href="https://fonts.googleapis.com/css2?family=Public+Sans:wght@300;400;500;600;700;900&display=swap" rel="stylesheet"/>
    <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet"/>
    <script id="tailwind-config">
        tailwind.config = {
            darkMode: "class",
            theme: {
                extend: {
                    colors: {
                        "primary": "#ec5b13",
                        "brand-mint": "#e6f4f1",
                        "brand-blue": "#e1f5fe",
                        "brand-pink": "#fce4ec",
                        "background-light": "#fcfaf9",
                        "background-dark": "#221610",
                        "text-main": "#3e2723",
                        "accent-soft": "#7fb8ad"
                    },
                    fontFamily: {
                        "display": ["Public Sans", "sans-serif"]
                    },
                },
            },
        }
    </script>
    <style>
        body { font-family: "Public Sans", sans-serif; }
        .material-symbols-outlined { font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24; }
    </style>
    {% block extra_css %}{% endblock %}
</head>
<body class="bg-background-light dark:bg-background-dark text-slate-900 dark:text-slate-100">
    <div class="relative flex min-h-screen w-full flex-col overflow-x-hidden">
        <!-- Top Navigation Bar -->
        <header class="sticky top-0 z-50 w-full border-b border-slate-200 dark:border-slate-800 bg-white/80 dark:bg-background-dark/80 backdrop-blur-md px-6 md:px-10 py-3">
            <div class="max-w-[1280px] mx-auto flex items-center justify-between gap-4">
                <div class="flex items-center gap-8">
                    <a href="{% url 'baby:home' %}" class="flex items-center gap-2 text-primary">
                        <span class="material-symbols-outlined text-3xl">child_care</span>
                        <h2 class="text-xl font-black leading-tight tracking-tight text-slate-900 dark:text-slate-100">Permutas Baby</h2>
                    </a>
                    <div class="hidden lg:flex w-72">
                        <form action="{% url 'baby:lista_produtos' %}" method="get" class="relative w-full">
                            <div class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none text-slate-400">
                                <span class="material-symbols-outlined text-xl">search</span>
                            </div>
                            <input name="q" class="block w-full pl-10 pr-4 py-2 bg-slate-100 dark:bg-slate-800 border-none rounded-xl focus:ring-2 focus:ring-primary/50 text-sm" placeholder="Buscar fraldas, carrinhos..." type="text"/>
                        </form>
                    </div>
                </div>
                <div class="flex items-center gap-6 lg:gap-10">
                    <nav class="hidden md:flex items-center gap-8">
                        <a class="text-sm font-semibold hover:text-primary transition-colors" href="{% url 'baby:lista_produtos' %}">Trocas</a>
                        {% if user.is_authenticated %}
                            <a class="text-sm font-semibold hover:text-primary transition-colors" href="{% url 'baby:meus_produtos' %}">Meus Anúncios</a>
                            <a class="text-sm font-semibold hover:text-primary transition-colors" href="{% url 'baby:minhas_trocas' %}">Minhas Trocas</a>
                        {% endif %}
                    </nav>
                    {% if user.is_authenticated %}
                        <div class="flex items-center gap-4">
                            <a href="{% url 'baby:criar_produto' %}" class="px-4 py-2 bg-primary text-white rounded-xl font-bold text-sm hover:bg-primary/90 transition-colors">
                                Anunciar
                            </a>
                            <div class="relative group">
                                <button class="size-10 rounded-full bg-brand-mint border-2 border-white shadow-sm overflow-hidden">
                                    {% if user.foto %}
                                        <img class="w-full h-full object-cover" src="{{ user.foto.url }}" alt="{{ user.username }}">
                                    {% else %}
                                        <span class="material-symbols-outlined text-primary">person</span>
                                    {% endif %}
                                </button>
                                <div class="absolute right-0 mt-2 w-48 bg-white rounded-xl shadow-lg border border-slate-100 opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all z-50">
                                    <a href="{% url 'baby:meus_produtos' %}" class="block px-4 py-2 text-sm hover:bg-slate-50">Meus Produtos</a>
                                    <a href="{% url 'baby:meus_favoritos' %}" class="block px-4 py-2 text-sm hover:bg-slate-50">Favoritos</a>
                                    <hr class="my-1">
                                    <form method="post" action="{% url 'users:logout' %}">
                                        {% csrf_token %}
                                        <button type="submit" class="block w-full text-left px-4 py-2 text-sm text-red-600 hover:bg-red-50">Sair</button>
                                    </form>
                                </div>
                            </div>
                        </div>
                    {% else %}
                        <div class="flex items-center gap-4">
                            <a href="{% url 'users:login' %}" class="text-sm font-semibold hover:text-primary transition-colors">Entrar</a>
                            <a href="{% url 'users:register' %}" class="px-4 py-2 bg-primary text-white rounded-xl font-bold text-sm hover:bg-primary/90 transition-colors">Cadastrar</a>
                        </div>
                    {% endif %}
                </div>
            </div>
        </header>

        {% if messages %}
            <div class="max-w-[1280px] mx-auto w-full px-6 md:px-10 mt-4">
                {% for message in messages %}
                    <div class="p-4 rounded-xl mb-2 {% if message.tags == 'success' %}bg-green-100 text-green-800{% elif message.tags == 'error' %}bg-red-100 text-red-800{% else %}bg-blue-100 text-blue-800{% endif %}">
                        {{ message }}
                    </div>
                {% endfor %}
            </div>
        {% endif %}

        <main class="max-w-[1280px] mx-auto w-full px-6 md:px-10 py-8">
            {% block content %}{% endblock %}
        </main>

        <footer class="bg-white dark:bg-slate-900 border-t border-slate-200 dark:border-slate-800 py-12 px-10 mt-auto">
            <div class="max-w-[1280px] mx-auto grid grid-cols-1 md:grid-cols-4 gap-12">
                <div class="col-span-1 md:col-span-1 space-y-4">
                    <div class="flex items-center gap-2 text-primary">
                        <span class="material-symbols-outlined text-2xl font-bold">child_care</span>
                        <h2 class="text-lg font-black tracking-tight text-slate-900 dark:text-slate-100">Permutas Baby</h2>
                    </div>
                    <p class="text-sm text-slate-500 leading-relaxed">
                        Conectando famílias para uma maternidade mais colaborativa e sustentável.
                    </p>
                </div>
                <div>
                    <h4 class="font-bold mb-4">Sobre</h4>
                    <ul class="space-y-2 text-sm text-slate-500">
                        <li><a class="hover:text-primary transition-colors" href="{% url 'sobre' %}">Sobre</a></li>
                        <li><a class="hover:text-primary transition-colors" href="{% url 'sobre' %}#como-funciona">Como funciona</a></li>
                    </ul>
                </div>
                <div>
                    <h4 class="font-bold mb-4">Ajuda</h4>
                    <ul class="space-y-2 text-sm text-slate-500">
                        <li><a class="hover:text-primary transition-colors" href="{% url 'ajuda' %}">Ajuda</a></li>
                        <li><a class="hover:text-primary transition-colors" href="{% url 'ajuda' %}">Termos de uso</a></li>
                    </ul>
                </div>
                <div>
                    <h4 class="font-bold mb-4">Siga-nos</h4>
                    <div class="flex gap-4">
                        <a class="size-10 rounded-full bg-brand-mint flex items-center justify-center text-primary hover:bg-primary hover:text-white transition-all" href="#">
                            <span class="material-symbols-outlined">share</span>
                        </a>
                        <a class="size-10 rounded-full bg-brand-blue flex items-center justify-center text-blue-600 hover:bg-blue-600 hover:text-white transition-all" href="#">
                            <span class="material-symbols-outlined">alternate_email</span>
                        </a>
                    </div>
                </div>
            </div>
            <div class="max-w-[1280px] mx-auto mt-12 pt-8 border-t border-slate-100 dark:border-slate-800 text-center text-xs text-slate-400">
                © 2024 Permutas Baby. Todos os direitos reservados.
            </div>
        </footer>
    </div>
    {% block extra_js %}{% endblock %}
</body>
</html>
```

---

## 2. Templates do Aplicativo (Baby)

### 2.1 templates/baby/home.html
*Página inicial com vitrine de produtos e categorias.*

```html
{% extends 'baby/base_baby.html' %}

{% block title %}Início - Permutas Baby{% endblock %}

{% block content %}
<!-- Hero Banner -->
<section class="mb-10 rounded-2xl overflow-hidden bg-brand-mint dark:bg-primary/10 border border-brand-mint dark:border-primary/20">
    <div class="flex flex-col md:flex-row items-center gap-8 p-8 md:p-12">
        <div class="flex-1 space-y-6">
            <span class="inline-block px-4 py-1 rounded-full bg-white dark:bg-slate-800 text-xs font-bold text-primary tracking-wider uppercase">Comunidade de Pais</span>
            <h1 class="text-4xl md:text-5xl lg:text-6xl font-black text-slate-900 dark:text-slate-100 leading-[1.1]">
                Troque o que sobrou pelo que seu <span class="text-primary">bebê precisa</span>
            </h1>
            <p class="text-lg text-slate-600 dark:text-slate-400 max-w-lg">
                A plataforma amiga para pais trocarem fraldas, roupas e acessórios de forma segura, sustentável e econômica.
            </p>
            <div class="flex flex-wrap gap-4">
                <a href="{% url 'baby:lista_produtos' %}" class="px-8 py-4 bg-primary text-white rounded-xl font-bold text-lg shadow-lg shadow-primary/30 hover:scale-105 transition-transform">
                    Começar Troca
                </a>
                <a href="{% url 'sobre' %}#como-funciona" class="px-8 py-4 bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 text-slate-700 dark:text-slate-200 rounded-xl font-bold text-lg hover:bg-slate-50 transition-colors">
                    Como funciona?
                </a>
            </div>
        </div>
        <div class="flex-1 w-full max-w-md">
            <div class="aspect-square bg-white/50 dark:bg-slate-800/50 rounded-2xl p-4 rotate-3 shadow-xl">
                <img class="w-full h-full object-cover rounded-xl -rotate-3 hover:rotate-0 transition-transform duration-500" src="https://example.com/hero.jpg" alt="Baby"/>
            </div>
        </div>
    </div>
</section>

<!-- Categories -->
{% if categorias %}
<section class="mb-10">
    <h2 class="text-2xl font-bold tracking-tight mb-6">Categorias</h2>
    <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-4">
        {% for categoria in categorias_topo %}
            <a href="?categoria={{ categoria.id }}" class="flex flex-col items-center p-4 bg-white rounded-xl border border-slate-100 hover:border-primary/30 hover:shadow-lg hover:shadow-primary/5 transition-all">
                <span class="material-symbols-outlined text-3xl text-primary mb-2">{{ categoria.icone|default:'category' }}</span>
                <span class="font-semibold text-sm text-center">{{ categoria.nome }}</span>
            </a>
        {% endfor %}
    </div>
</section>
{% endif %}

<!-- Product Grid -->
<div class="flex flex-col lg:flex-row gap-10">
    <div class="flex-1">
        <h2 class="text-2xl font-bold tracking-tight mb-8">Produtos em Destaque</h2>
        {% if produtos %}
            <div class="grid grid-cols-1 sm:grid-cols-2 xl:grid-cols-3 gap-6">
                {% for produto in produtos %}
                    <a href="{% url 'baby:produto_detalhe' pk=produto.pk slug=produto.slug %}" class="group bg-white rounded-2xl overflow-hidden border border-slate-100 shadow-sm hover:shadow-xl transition-all duration-300">
                        <div class="aspect-[4/3] relative overflow-hidden">
                            {% if produto.imagem_principal %}
                                <img class="w-full h-full object-cover group-hover:scale-105 transition-transform" src="{{ produto.imagem_principal.url }}" alt="{{ produto.titulo }}"/>
                            {% endif %}
                        </div>
                        <div class="p-5">
                            <h3 class="font-bold text-lg mb-1">{{ produto.titulo }}</h3>
                            <div class="flex items-center gap-1 text-slate-500 text-sm mb-4">
                                <span class="material-symbols-outlined text-lg">location_on</span>
                                <span>{{ produto.cidade }}, {{ produto.estado }}</span>
                            </div>
                        </div>
                    </a>
                {% endfor %}
            </div>
        {% endif %}
    </div>
</div>
{% endblock %}
```

### 2.2 templates/baby/produto_detalhe.html
*Página de detalhes com sistema de proposta de troca.*

```html
{% extends 'baby/base_baby.html' %}

{% block title %}{{ produto.titulo }} - Permutas Baby{% endblock %}

{% block content %}
<div class="grid grid-cols-1 lg:grid-cols-2 gap-10">
    <!-- Product Images -->
    <div class="space-y-4">
        <div class="aspect-square rounded-2xl overflow-hidden bg-slate-100">
            {% if produto.imagem_principal %}
                <img id="main-image" class="w-full h-full object-cover" src="{{ produto.imagem_principal.url }}" alt="{{ produto.titulo }}"/>
            {% endif %}
        </div>
    </div>
    
    <!-- Product Info -->
    <div>
        <h1 class="text-3xl font-black text-slate-900 mb-4">{{ produto.titulo }}</h1>
        <div class="prose text-slate-600 mb-8">
            <h3 class="font-bold text-slate-900 mb-2">Descrição</h3>
            <p>{{ produto.descricao }}</p>
        </div>
        
        {% if produto.preferencias_troca %}
            <div class="bg-brand-mint rounded-xl p-4 mb-8">
                <h3 class="font-bold text-slate-900 mb-2">Preferências de Troca</h3>
                <p class="text-slate-600">{{ produto.preferencias_troca }}</p>
            </div>
        {% endif %}
        
        <!-- Actions -->
        {% if user.is_authenticated and user != produto.usuario %}
            <button onclick="document.getElementById('proposta-modal').classList.remove('hidden')" class="w-full py-4 bg-primary text-white rounded-xl font-bold text-lg shadow-lg">
                Propor Troca
            </button>
        {% endif %}
    </div>
</div>

<!-- Modal de Proposta -->
<div id="proposta-modal" class="fixed inset-0 bg-black/50 hidden z-50 flex items-center justify-center p-4">
    <div class="bg-white rounded-2xl max-w-lg w-full p-6">
        <h3 class="text-xl font-bold mb-4">Enviar Proposta de Troca</h3>
        <form method="post" action="{% url 'baby:criar_proposta' produto.pk %}">
            {% csrf_token %}
            <div class="mb-4">
                <label class="block text-sm font-bold mb-2">Item Oferecido</label>
                <select name="produto_oferecido" required class="w-full px-4 py-3 rounded-xl border">
                    {% for prod in meus_produtos_disponiveis %}
                        <option value="{{ prod.pk }}">{{ prod.titulo }}</option>
                    {% endfor %}
                </select>
            </div>
            <button type="submit" class="w-full py-3 bg-primary text-white rounded-xl font-bold">Enviar</button>
        </form>
    </div>
</div>
{% endblock %}
```

### 2.3 templates/baby/minhas_trocas.html
*Painel de gestão de propostas de troca (Recebidas/Enviadas).*

```html
{% extends 'baby/base_baby.html' %}

{% block content %}
<div class="max-w-4xl mx-auto">
    <h1 class="text-3xl font-black mb-8">Minhas Trocas</h1>
    
    <div class="flex gap-4 mb-8 border-b border-slate-200">
        <a href="?tab=recebidas" class="px-4 py-2 font-bold {% if tab == 'recebidas' %}border-b-2 border-primary text-primary{% endif %}">Recebidas</a>
        <a href="?tab=enviadas" class="px-4 py-2 font-bold {% if tab == 'enviadas' %}border-b-2 border-primary text-primary{% endif %}">Enviadas</a>
    </div>
    
    {% for proposta in propostas %}
        <div class="bg-white rounded-xl border p-4 mb-4 flex items-center gap-4">
            <div class="flex-1">
                <p class="font-bold">{{ proposta.produto_oferecido.titulo }}</p>
                <p class="text-sm text-slate-500">↔ {{ proposta.produto_desejado.titulo }}</p>
                <span class="text-xs font-bold uppercase p-1 rounded bg-slate-100">{{ proposta.get_status_display }}</span>
            </div>
            {% if tab == 'recebidas' and proposta.status == 'pendente' %}
                <div class="flex gap-2">
                    <form method="post" action="{% url 'baby:aceitar_proposta' proposta.pk %}">
                        {% csrf_token %}<button class="bg-green-500 text-white px-3 py-1 rounded">Aceitar</button>
                    </form>
                </div>
            {% endif %}
        </div>
    {% endfor %}
</div>
{% endblock %}
```

---

## 3. Templates Institucionais e Fluxo de Usuário

### 3.1 templates/sobre.html
*Página institucional explicando o conceito de economia circular do projeto.*

```html
{% extends "baby/base_baby.html" %}

{% block title %}Sobre - Permutas Baby{% endblock %}

{% block content %}
<div class="max-w-[1200px] mx-auto">
    <div class="py-16 text-center">
        <h1 class="text-5xl font-black mb-6">Sobre a Permutas Baby</h1>
        <p class="text-lg text-slate-600 max-w-2xl mx-auto">
            A Permutas Baby nasceu do desejo de criar um mundo onde a parentalidade seja mais leve, econômica e consciente. 
            Promovemos a economia circular conectando famílias para trocar itens que bebês cresceram rápido demais para usar.
        </p>
    </div>
    
    <div class="grid grid-cols-1 md:grid-cols-3 gap-8 py-10">
        <div class="bg-white p-8 rounded-2xl shadow-sm border">
            <span class="material-symbols-outlined text-primary text-4xl mb-4">add_photo_alternate</span>
            <h3 class="font-bold text-xl mb-2">1. Cadastre</h3>
            <p class="text-slate-500">Publique fotos do que seu bebê não usa mais.</p>
        </div>
        <div class="bg-white p-8 rounded-2xl shadow-sm border">
            <span class="material-symbols-outlined text-primary text-4xl mb-4">volunteer_activism</span>
            <h3 class="font-bold text-xl mb-2">2. Encontre</h3>
            <p class="text-slate-500">Navegue e proponha trocas pelo que precisa.</p>
        </div>
        <div class="bg-white p-8 rounded-2xl shadow-sm border">
            <span class="material-symbols-outlined text-primary text-4xl mb-4">local_shipping</span>
            <h3 class="font-bold text-xl mb-2">3. Troque</h3>
            <p class="text-slate-500">Combine a entrega e ajude o planeta.</p>
        </div>
    </div>
</div>
{% endblock %}
```

### 3.2 templates/rastreio.html
*Página de acompanhamento logístico da troca em tempo real.*

```html
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <title>Rastreio da Troca - Permutas Baby</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined" rel="stylesheet"/>
</head>
<body class="bg-slate-50 min-h-screen p-8">
    <div class="max-w-4xl mx-auto">
        <h1 class="text-3xl font-black mb-10">Rastreio da Troca #PB-88219</h1>
        
        <div class="bg-white rounded-2xl shadow-sm border p-6 mb-8">
            <h2 class="font-bold text-xl mb-6 flex items-center gap-2">
                <span class="material-symbols-outlined text-primary">local_shipping</span>
                Status do Envio
            </h2>
            <div class="relative pl-8 border-l-2 border-slate-200 space-y-8">
                <div class="relative">
                    <div class="absolute -left-[37px] size-4 rounded-full bg-primary border-2 border-white"></div>
                    <p class="font-bold">Proposta Aceita</p>
                    <p class="text-slate-500 text-sm">12 de Outubro - 14:30</p>
                </div>
                <div class="relative">
                    <div class="absolute -left-[37px] size-4 rounded-full bg-primary animate-pulse"></div>
                    <p class="text-primary font-bold">Em Trânsito</p>
                    <p class="text-slate-500 text-sm">A caminho do destinatário</p>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
```
