import os
import shutil
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from baby.models import Categoria, Produto, Marca

User = get_user_model()


class Command(BaseCommand):
    help = 'Populate database with test users and products'

    def handle(self, *args, **options):
        self.create_users()
        self.create_categories()
        self.create_products()

    def create_users(self):
        users_data = [
            {'username': 'joao_silva', 'email': 'joao@teste.com', 'first_name': 'João', 'last_name': 'Silva'},
            {'username': 'maria_santos', 'email': 'maria@teste.com', 'first_name': 'Maria', 'last_name': 'Santos'},
            {'username': 'pedro_oliveira', 'email': 'pedro@teste.com', 'first_name': 'Pedro', 'last_name': 'Oliveira'},
            {'username': 'ana_ferreira', 'email': 'ana@teste.com', 'first_name': 'Ana', 'last_name': 'Ferreira'},
            {'username': 'carlos_souza', 'email': 'carlos@teste.com', 'first_name': 'Carlos', 'last_name': 'Souza'},
        ]

        for user_data in users_data:
            user, created = User.objects.get_or_create(
                username=user_data['username'],
                defaults={
                    'email': user_data['email'],
                    'first_name': user_data['first_name'],
                    'last_name': user_data['last_name'],
                    'tipo_usuario': 'baby',
                    'cidade': 'São Paulo',
                    'estado': 'SP',
                }
            )
            if created:
                user.set_password('senha123')
                user.save()
                self.stdout.write(self.style.SUCCESS(f'Created user: {user.username}'))
            else:
                self.stdout.write(f'User already exists: {user.username}')

    def create_categories(self):
        categories_data = [
            {'nome': 'Roupas', 'icone': 'checkroom', 'cor': '#ec5b13'},
            {'nome': 'Calçados', 'icone': 'child_care', 'cor': '#8b5cf6'},
            {'nome': 'Brinquedos', 'icone': 'toys', 'cor': '#10b981'},
            {'nome': 'Carrinhos', 'icone': 'directions_car', 'cor': '#f59e0b'},
            {'nome': 'Berços', 'icone': 'bed', 'cor': '#3b82f6'},
            {'nome': 'Alimentação', 'icone': 'restaurant', 'cor': '#ef4444'},
            {'nome': 'Higiene', 'icone': 'spa', 'cor': '#ec4899'},
            {'nome': 'Livros', 'icone': 'menu_book', 'cor': '#6366f1'},
            {'nome': 'Acessórios', 'icone': 'watch', 'cor': '#14b8a6'},
            {'nome': 'Móveis', 'icone': 'chair', 'cor': '#78716c'},
        ]

        for cat_data in categories_data:
            cat, created = Categoria.objects.get_or_create(
                slug=cat_data['nome'].lower(),
                defaults={
                    'nome': cat_data['nome'],
                    'icone': cat_data['icone'],
                    'cor': cat_data['cor'],
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created category: {cat.nome}'))

    def create_products(self):
        users = list(User.objects.all())
        categories = list(Categoria.objects.all())

        if not users:
            self.stdout.write(self.style.ERROR('No users found! Run create_users first.'))
            return

        if not categories:
            self.stdout.write(self.style.ERROR('No categories found! Run create_categories first.'))
            return

        products_data = [
            {'titulo': 'Macacão Bebê Menino 6-9m', 'categoria': 'Roupas', 'tamanho': '6_9m', 'genero': 'masculino', 'condicao': 'seminovo'},
            {'titulo': 'Vestido Floral 12-18m', 'categoria': 'Roupas', 'tamanho': '12_18m', 'genero': 'feminino', 'condicao': 'novo'},
            {'titulo': 'Conjunto Body + Calça 3-6m', 'categoria': 'Roupas', 'tamanho': '3_6m', 'genero': 'unisex', 'condicao': 'usado_otimo'},
            {'titulo': 'Jaqueta de Moletom 18-24m', 'categoria': 'Roupas', 'tamanho': '18_24m', 'genero': 'unisex', 'condicao': 'seminovo'},
            {'titulo': 'Camiseta Estampada 2t', 'categoria': 'Roupas', 'tamanho': '2t', 'genero': 'masculino', 'condicao': 'usado_bom'},
            {'titulo': 'Saia Tutu 18-24m', 'categoria': 'Roupas', 'tamanho': '18_24m', 'genero': 'feminino', 'condicao': 'novo'},
            {'titulo': 'Calça Jeans 3t', 'categoria': 'Roupas', 'tamanho': '3t', 'genero': 'unisex', 'condicao': 'seminovo'},
            {'titulo': 'Body Manga Longa 0-3m', 'categoria': 'Roupas', 'tamanho': '0_3m', 'genero': 'unisex', 'condicao': 'usado_otimo'},
            {'titulo': 'Pijama Animais 4t', 'categoria': 'Roupas', 'tamanho': '4t', 'genero': 'unisex', 'condicao': 'usado_bom'},
            {'titulo': 'Vestido Junina 5t', 'categoria': 'Roupas', 'tamanho': '5t', 'genero': 'feminino', 'condicao': 'novo'},

            {'titulo': 'Sapatinho Lã RN', 'categoria': 'Calçados', 'tamanho': 'rn', 'genero': 'unisex', 'condicao': 'novo'},
            {'titulo': 'Tênis Baby 0-3m', 'categoria': 'Calçados', 'tamanho': '0_3m', 'genero': 'unisex', 'condicao': 'seminovo'},
            {'titulo': 'Sandálias 12-18m', 'categoria': 'Calçados', 'tamanho': '12_18m', 'genero': 'feminino', 'condicao': 'usado_otimo'},
            {'titulo': 'Bota Inverno 18-24m', 'categoria': 'Calçados', 'tamanho': '18_24m', 'genero': 'masculino', 'condicao': 'seminovo'},
            {'titulo': 'Pantufa 2t', 'categoria': 'Calçados', 'tamanho': '2t', 'genero': 'unisex', 'condicao': 'usado_bom'},
            {'titulo': 'Chinelo 3t', 'categoria': 'Calçados', 'tamanho': '3t', 'genero': 'masculino', 'condicao': 'novo'},
            {'titulo': 'Mocassim 4t', 'categoria': 'Calçados', 'tamanho': '4t', 'genero': 'feminino', 'condicao': 'usado_otimo'},
            {'titulo': 'Sapatilha Laço 5t', 'categoria': 'Calçados', 'tamanho': '5t', 'genero': 'feminino', 'condicao': 'novo'},
            {'titulo': 'Coturno Baby 9-12m', 'categoria': 'Calçados', 'tamanho': '9_12m', 'genero': 'unisex', 'condicao': 'seminovo'},
            {'titulo': 'Rasteirinha Glitter 5t', 'categoria': 'Calçados', 'tamanho': '5t', 'genero': 'feminino', 'condicao': 'usado_bom'},

            {'titulo': 'Pelúcia Urso Grande', 'categoria': 'Brinquedos', 'genero': 'unisex', 'condicao': 'seminovo'},
            {'titulo': 'Carrinho Hot Wheels', 'categoria': 'Brinquedos', 'genero': 'masculino', 'condicao': 'usado_otimo'},
            {'titulo': 'Boneca Bebê', 'categoria': 'Brinquedos', 'genero': 'feminino', 'condicao': 'novo'},
            {'titulo': 'Bloco de Construção', 'categoria': 'Brinquedos', 'genero': 'unisex', 'condicao': 'seminovo'},
            {'titulo': 'Triciclo Infantile', 'categoria': 'Brinquedos', 'genero': 'unisex', 'condicao': 'usado_bom'},
            {'titulo': 'Quepe Educativo', 'categoria': 'Brinquedos', 'genero': 'unisex', 'condicao': 'novo'},
            {'titulo': 'Piano Brinquedo', 'categoria': 'Brinquedos', 'genero': 'unisex', 'condicao': 'seminovo'},
            {'titulo': 'Parque Jump', 'categoria': 'Brinquedos', 'genero': 'unisex', 'condicao': 'usado_otimo'},
            {'titulo': 'Tapete Musical', 'categoria': 'Brinquedos', 'genero': 'unisex', 'condicao': 'novo'},
            {'titulo': 'Bola Pitoco', 'categoria': 'Brinquedos', 'genero': 'unisex', 'condicao': 'seminovo'},

            {'titulo': 'Carrinho de Bebê Urban', 'categoria': 'Carrinhos', 'genero': 'unisex', 'condicao': 'seminovo'},
            {'titulo': 'Carrinho Travel System', 'categoria': 'Carrinhos', 'genero': 'unisex', 'condicao': 'usado_otimo'},
            {'titulo': 'Carrinho Gêmeos', 'categoria': 'Carrinhos', 'genero': 'unisex', 'condicao': 'usado_bom'},
            {'titulo': 'Carrinho Côco', 'categoria': 'Carrinhos', 'genero': 'unisex', 'condicao': 'novo'},
            {'titulo': 'Carrinho Articulado', 'categoria': 'Carrinhos', 'genero': 'unisex', 'condicao': 'seminovo'},
            {'titulo': 'Bebê Conforto', 'categoria': 'Carrinhos', 'genero': 'unisex', 'condicao': 'usado_otimo'},
            {'titulo': 'Cadeirinha Auto 9-36kg', 'categoria': 'Carrinhos', 'genero': 'unisex', 'condicao': 'seminovo'},
            {'titulo': 'Base Isofix', 'categoria': 'Carrinhos', 'genero': 'unisex', 'condicao': 'novo'},
            {'titulo': 'Carrinho de Boneca', 'categoria': 'Carrinhos', 'genero': 'feminino', 'condicao': 'usado_bom'},
            {'titulo': 'Carrinho Mão Baby', 'categoria': 'Carrinhos', 'genero': 'unisex', 'condicao': 'novo'},

            {'titulo': 'Berço Americano', 'categoria': 'Berços', 'genero': 'unisex', 'condicao': 'seminovo'},
            {'titulo': 'Mini Berço', 'categoria': 'Berços', 'genero': 'unisex', 'condicao': 'usado_otimo'},
            {'titulo': 'Cômoda Trocador', 'categoria': 'Berços', 'genero': 'unisex', 'condicao': 'novo'},
            {'titulo': 'Berço Portátil', 'categoria': 'Berços', 'genero': 'unisex', 'condicao': 'seminovo'},
            {'titulo': 'Travesseiro Anti-refluxo', 'categoria': 'Berços', 'genero': 'unisex', 'condicao': 'novo'},
            {'titulo': 'Colchão Berço', 'categoria': 'Berços', 'genero': 'unisex', 'condicao': 'usado_bom'},
            {'titulo': 'Mosquiteiro Berço', 'categoria': 'Berços', 'genero': 'unisex', 'condicao': 'seminovo'},
            {'titulo': 'Grades Proteção Berço', 'categoria': 'Berços', 'genero': 'unisex', 'condicao': 'novo'},
            {'titulo': 'Redutor Berço', 'categoria': 'Berços', 'genero': 'unisex', 'condicao': 'usado_otimo'},
            {'titulo': 'Almofada Berço', 'categoria': 'Berços', 'genero': 'unisex', 'condicao': 'seminovo'},

            {'titulo': 'Mamadeira Anti-colic 240ml', 'categoria': 'Alimentação', 'genero': 'unisex', 'condicao': 'novo'},
            {'titulo': 'Kit Colheres Silicone', 'categoria': 'Alimentação', 'genero': 'unisex', 'condicao': 'novo'},
            {'titulo': 'Prato com Ventosa', 'categoria': 'Alimentação', 'genero': 'unisex', 'condicao': 'seminovo'},
            {'titulo': 'Copinho Treinamento', 'categoria': 'Alimentação', 'genero': 'unisex', 'condicao': 'usado_otimo'},
            {'titulo': 'Alimento Instantâneo', 'categoria': 'Alimentação', 'genero': 'unisex', 'condicao': 'novo'},
            {'titulo': 'Fórmula Infantil 1', 'categoria': 'Alimentação', 'genero': 'unisex', 'condicao': 'novo'},
            {'titulo': 'Papinha Industrializada', 'categoria': 'Alimentação', 'genero': 'unisex', 'condicao': 'novo'},
            {'titulo': 'Biscoito Fortificado', 'categoria': 'Alimentação', 'genero': 'unisex', 'condicao': 'usado_bom'},
            {'titulo': 'Torradeira Fun', 'categoria': 'Alimentação', 'genero': 'unisex', 'condicao': 'seminovo'},
            {'titulo': 'Kit Louça Infantil', 'categoria': 'Alimentação', 'genero': 'unisex', 'condicao': 'novo'},

            {'titulo': 'Fraldas Pants M', 'categoria': 'Higiene', 'genero': 'unisex', 'condicao': 'novo'},
            {'titulo': 'Pomada Assadura', 'categoria': 'Higiene', 'genero': 'unisex', 'condicao': 'novo'},
            {'titulo': 'Sabonete Líquido Baby', 'categoria': 'Higiene', 'genero': 'unisex', 'condicao': 'novo'},
            {'titulo': 'Shampoo Neutro', 'categoria': 'Higiene', 'genero': 'unisex', 'condicao': 'seminovo'},
            {'titulo': 'Escova Cabelo Soft', 'categoria': 'Higiene', 'genero': 'unisex', 'condicao': 'usado_otimo'},
            {'titulo': 'Cortador Unhas', 'categoria': 'Higiene', 'genero': 'unisex', 'condicao': 'novo'},
            {'titulo': 'Termômetro Digital', 'categoria': 'Higiene', 'genero': 'unisex', 'condicao': 'seminovo'},
            {'titulo': 'Aspirador Nasal', 'categoria': 'Higiene', 'genero': 'unisex', 'condicao': 'usado_bom'},
            {'titulo': 'Haste Cotonetes', 'categoria': 'Higiene', 'genero': 'unisex', 'condicao': 'novo'},
            {'titulo': 'Kit Higiene Completo', 'categoria': 'Higiene', 'genero': 'unisex', 'condicao': 'novo'},

            {'titulo': 'Livro Sensorial', 'categoria': 'Livros', 'genero': 'unisex', 'condicao': 'novo'},
            {'titulo': 'Livro de Banho', 'categoria': 'Livros', 'genero': 'unisex', 'condicao': 'usado_otimo'},
            {'titulo': 'Cartilha de Alfabetização', 'categoria': 'Livros', 'genero': 'unisex', 'condicao': 'seminovo'},
            {'titulo': 'Livro de Colorir', 'categoria': 'Livros', 'genero': 'unisex', 'condicao': 'usado_bom'},
            {'titulo': 'Pack Livros Infantis 5un', 'categoria': 'Livros', 'genero': 'unisex', 'condicao': 'novo'},
            {'titulo': 'Dicionário Infantil', 'categoria': 'Livros', 'genero': 'unisex', 'condicao': 'seminovo'},
            {'titulo': 'Biblioteca Mínima', 'categoria': 'Livros', 'genero': 'unisex', 'condicao': 'usado_otimo'},
            {'titulo': 'Livro Trilha Sensorial', 'categoria': 'Livros', 'genero': 'unisex', 'condicao': 'novo'},
            {'titulo': 'Contos Clássicos', 'categoria': 'Livros', 'genero': 'unisex', 'condicao': 'seminovo'},
            {'titulo': 'Enciclopédia Baby', 'categoria': 'Livros', 'genero': 'unisex', 'condicao': 'usado_bom'},

            {'titulo': 'Chapeu Palha Summer', 'categoria': 'Acessórios', 'genero': 'unisex', 'condicao': 'novo'},
            {'titulo': 'Óculos Sol Baby', 'categoria': 'Acessórios', 'genero': 'unisex', 'condicao': 'novo'},
            {'titulo': 'Luva Proteção UV', 'categoria': 'Acessórios', 'genero': 'unisex', 'condicao': 'seminovo'},
            {'titulo': 'Presilha Cabelo', 'categoria': 'Acessórios', 'genero': 'feminino', 'condicao': 'usado_otimo'},
            {'titulo': 'Tiara Floral', 'categoria': 'Acessórios', 'genero': 'feminino', 'condicao': 'novo'},
            {'titulo': 'Laço Big Hair', 'categoria': 'Acessórios', 'genero': 'feminino', 'condicao': 'usado_bom'},
            {'titulo': 'Bolsa Maternidade', 'categoria': 'Acessórios', 'genero': 'unisex', 'condicao': 'seminovo'},
            {'titulo': 'Mochila Creche', 'categoria': 'Acessórios', 'genero': 'unisex', 'condicao': 'novo'},
            {'titulo': 'Lancheira Kids', 'categoria': 'Acessórios', 'genero': 'unisex', 'condicao': 'usado_otimo'},
            {'titulo': 'Garrafa Água Infantil', 'categoria': 'Acessórios', 'genero': 'unisex', 'condicao': 'novo'},

            {'titulo': 'Poltrona Amamentação', 'categoria': 'Móveis', 'genero': 'unisex', 'condicao': 'seminovo'},
            {'titulo': 'Banqueta Alimentação', 'categoria': 'Móveis', 'genero': 'unisex', 'condicao': 'usado_otimo'},
            {'titulo': 'Box Organizador', 'categoria': 'Móveis', 'genero': 'unisex', 'condicao': 'novo'},
            {'titulo': 'Guarda Roupa Mini', 'categoria': 'Móveis', 'genero': 'unisex', 'condicao': 'seminovo'},
            {'titulo': 'Cômoda Mini', 'categoria': 'Móveis', 'genero': 'unisex', 'condicao': 'usado_bom'},
            {'titulo': 'Estante Brinquedos', 'categoria': 'Móveis', 'genero': 'unisex', 'condicao': 'novo'},
            {'titulo': 'Pufê Estofado', 'categoria': 'Móveis', 'genero': 'unisex', 'condicao': 'usado_otimo'},
            {'titulo': 'Tapete Emborrachado', 'categoria': 'Móveis', 'genero': 'unisex', 'condicao': 'seminovo'},
            {'titulo': 'Parede Divisória', 'categoria': 'Móveis', 'genero': 'unisex', 'condicao': 'novo'},
            {'titulo': 'Ventilador Coluna Baby', 'categoria': 'Móveis', 'genero': 'unisex', 'condicao': 'usado_bom'},
        ]

        existing_count = Produto.objects.count()
        target_count = 100
        products_to_create = target_count - existing_count

        if products_to_create > 0:
            for i in range(products_to_create):
                data = products_data[i % len(products_data)]
                user = users[i % len(users)]
                categoria = next((c for c in categories if c.nome == data['categoria']), categories[0])

                titulo = f"{data['titulo']} ({user.username})" if i >= len(products_data) else data['titulo']

                produto = Produto(
                    usuario=user,
                    titulo=titulo,
                    descricao=f'{data["titulo"]} em excelente estado. Perfeito para troca!',
                    categoria=categoria,
                    tamanho_roupa=data.get('tamanho', ''),
                    genero=data['genero'],
                    condicao=data['condicao'],
                    cidade=user.cidade or 'São Paulo',
                    estado=user.estado or 'SP',
                    status='disponivel',
                )

                img_path = 'produtos/exemplo.png'
                produto.imagem_principal = img_path

                produto.save()
                self.stdout.write(f'Created product: {produto.titulo}')

        self.stdout.write(self.style.SUCCESS(f'Total products in DB: {Produto.objects.count()}'))
