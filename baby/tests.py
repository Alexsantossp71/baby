from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from baby.models import Categoria, Produto, PropostaTroca, ProdutoFavorito

User = get_user_model()


class ProdutoModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', email='test@test.com', password='TestPass123!'
        )
        self.categoria = Categoria.objects.create(nome='Fraldas', slug='fraldas')
        self.produto = Produto.objects.create(
            titulo='Fralda Pampers G',
            descricao='Pacote fechado',
            categoria=self.categoria,
            usuario=self.user,
            cidade='SP',
            estado='SP',
            imagem_principal='produtos/test.jpg',
        )

    def test_slug_gerado_automaticamente(self):
        """Slug deve ser gerado a partir do título no save()."""
        self.assertEqual(self.produto.slug, 'fralda-pampers-g')

    def test_str_retorna_titulo(self):
        self.assertEqual(str(self.produto), 'Fralda Pampers G')

    def test_status_padrao_disponivel(self):
        self.assertEqual(self.produto.status, 'disponivel')

    def test_uuid_como_pk(self):
        """PK deve ser UUID, não inteiro sequencial."""
        import uuid
        self.assertIsInstance(self.produto.pk, uuid.UUID)


class PropostaTrocaModelTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(
            username='user1', email='u1@test.com', password='Pass123!'
        )
        self.user2 = User.objects.create_user(
            username='user2', email='u2@test.com', password='Pass123!'
        )
        self.cat = Categoria.objects.create(nome='Roupas', slug='roupas')
        self.produto1 = Produto.objects.create(
            titulo='Produto 1', descricao='desc', categoria=self.cat,
            usuario=self.user1, cidade='SP', estado='SP',
            imagem_principal='produtos/t1.jpg',
        )
        self.produto2 = Produto.objects.create(
            titulo='Produto 2', descricao='desc', categoria=self.cat,
            usuario=self.user2, cidade='SP', estado='SP',
            imagem_principal='produtos/t2.jpg',
        )
        self.proposta = PropostaTroca.objects.create(
            proponente=self.user2,
            proprietario=self.user1,
            produto_oferecido=self.produto2,
            produto_desejado=self.produto1,
            mensagem='Quero trocar!',
        )

    def test_aceitar_muda_status_produtos(self):
        """Aceitar proposta deve marcar ambos os produtos como 'trocado'."""
        self.proposta.aceitar()
        self.produto1.refresh_from_db()
        self.produto2.refresh_from_db()
        self.assertEqual(self.proposta.status, 'aceita')
        self.assertEqual(self.produto1.status, 'trocado')
        self.assertEqual(self.produto2.status, 'trocado')

    def test_rejeitar_com_motivo(self):
        self.proposta.rejeitar('Não tenho mais interesse')
        self.assertEqual(self.proposta.status, 'rejeitada')
        self.assertEqual(self.proposta.motivo_recusa, 'Não tenho mais interesse')

    def test_aceitar_rejeita_propostas_pendentes(self):
        """Aceitar deve rejeitar automaticamente outras propostas pendentes."""
        proposta2 = PropostaTroca.objects.create(
            proponente=self.user2, proprietario=self.user1,
            produto_oferecido=self.produto2, produto_desejado=self.produto1,
            mensagem='Outra proposta',
        )
        self.proposta.aceitar()
        proposta2.refresh_from_db()
        self.assertEqual(proposta2.status, 'rejeitada')


class HomeViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', email='test@test.com', password='TestPass123!'
        )
        self.cat = Categoria.objects.create(nome='Fraldas', slug='fraldas', ativa=True)

    def test_home_retorna_200(self):
        response = self.client.get(reverse('baby:home'))
        self.assertEqual(response.status_code, 200)

    def test_home_so_aceita_get(self):
        response = self.client.post(reverse('baby:home'))
        self.assertEqual(response.status_code, 405)

    def test_lista_produtos_paginada(self):
        response = self.client.get(reverse('baby:lista_produtos'))
        self.assertEqual(response.status_code, 200)

    def test_ordenacao_invalida_nao_quebra(self):
        """Parâmetro de ordenação inválido deve ser ignorado sem erro."""
        response = self.client.get(reverse('baby:home'), {'ordenacao': 'campo_invalido'})
        self.assertEqual(response.status_code, 200)


class CriarProdutoViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', email='test@test.com', password='TestPass123!'
        )
        self.cat = Categoria.objects.create(nome='Fraldas', slug='fraldas', ativa=True)

    def test_requer_login(self):
        response = self.client.get(reverse('baby:criar_produto'))
        self.assertEqual(response.status_code, 302)
        self.assertIn('/accounts/login/', response.url)

    def test_logado_retorna_200(self):
        self.client.login(username='test@test.com', password='TestPass123!')
        response = self.client.get(reverse('baby:criar_produto'))
        self.assertEqual(response.status_code, 200)


class FavoritarViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', email='test@test.com', password='TestPass123!'
        )
        self.cat = Categoria.objects.create(nome='Roupas', slug='roupas')
        self.produto = Produto.objects.create(
            titulo='Produto Fav', descricao='desc', categoria=self.cat,
            usuario=self.user, cidade='SP', estado='SP',
            imagem_principal='produtos/t1.jpg',
        )
        self.client.login(username='test@test.com', password='TestPass123!')

    def test_favoritar_incrementa_count(self):
        response = self.client.post(reverse('baby:favoritar_produto'), {'produto_id': self.produto.pk})
        self.assertEqual(response.status_code, 200)
        self.produto.refresh_from_db()
        self.assertEqual(self.produto.favorito_count, 1)

    def test_desfavoritar_decrementa_count(self):
        # Favoritar primeiro
        self.client.post(reverse('baby:favoritar_produto'), {'produto_id': self.produto.pk})
        # Desfavoritar
        self.client.post(reverse('baby:favoritar_produto'), {'produto_id': self.produto.pk})
        self.produto.refresh_from_db()
        self.assertEqual(self.produto.favorito_count, 0)

    def test_requer_post(self):
        response = self.client.get(reverse('baby:favoritar_produto'))
        self.assertEqual(response.status_code, 405)
