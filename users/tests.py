from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', email='test@test.com', password='TestPass123!',
            first_name='João', last_name='Silva'
        )

    def test_str_retorna_email(self):
        self.assertEqual(str(self.user), 'test@test.com')

    def test_get_full_name(self):
        self.assertEqual(self.user.get_full_name(), 'João Silva')

    def test_get_full_name_sem_nome(self):
        user2 = User.objects.create_user(username='u2', email='u2@t.com', password='P123!')
        self.assertEqual(user2.get_full_name(), 'u2')

    def test_get_initials(self):
        self.assertEqual(self.user.get_initials(), 'JS')

    def test_get_initials_sem_nome(self):
        user2 = User.objects.create_user(username='maria', email='m@t.com', password='P123!')
        self.assertEqual(user2.get_initials(), 'M')

    def test_email_unico(self):
        from django.db import IntegrityError
        with self.assertRaises(IntegrityError):
            User.objects.create_user(username='other', email='test@test.com', password='P123!')


class RegisterViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_register(self):
        response = self.client.get(reverse('users:register'))
        self.assertEqual(response.status_code, 200)

    def test_register_cria_usuario(self):
        response = self.client.post(reverse('users:register'), {
            'username': 'novousuario',
            'email': 'novo@test.com',
            'password': 'SenhaForte123!',
            'termos': True,
        })
        self.assertEqual(response.status_code, 302)  # redirect
        self.assertTrue(User.objects.filter(email='novo@test.com').exists())

    def test_register_redireciona_logado(self):
        User.objects.create_user(username='t', email='t@t.com', password='P123!')
        self.client.login(username='t@t.com', password='P123!')
        response = self.client.get(reverse('users:register'))
        self.assertEqual(response.status_code, 302)


class LoginViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', email='test@test.com', password='TestPass123!'
        )

    def test_get_login(self):
        response = self.client.get(reverse('users:login'))
        self.assertEqual(response.status_code, 200)

    def test_login_com_email(self):
        """Deve autenticar usando email (EmailOrUsernameModelBackend)."""
        response = self.client.post(reverse('users:login'), {
            'username': 'test@test.com',
            'password': 'TestPass123!',
        })
        self.assertEqual(response.status_code, 302)

    def test_login_redireciona_logado(self):
        self.client.login(username='test@test.com', password='TestPass123!')
        response = self.client.get(reverse('users:login'))
        self.assertEqual(response.status_code, 302)


class LogoutViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', email='test@test.com', password='TestPass123!'
        )

    def test_logout_requer_post(self):
        """Logout via GET deve retornar 405."""
        self.client.login(username='test@test.com', password='TestPass123!')
        response = self.client.get(reverse('users:logout'))
        self.assertEqual(response.status_code, 405)

    def test_logout_post_funciona(self):
        self.client.login(username='test@test.com', password='TestPass123!')
        response = self.client.post(reverse('users:logout'))
        self.assertEqual(response.status_code, 302)


class PerfilViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', email='test@test.com', password='TestPass123!'
        )

    def test_perfil_requer_login(self):
        response = self.client.get(reverse('users:perfil'))
        self.assertEqual(response.status_code, 302)

    def test_perfil_logado_retorna_200(self):
        self.client.login(username='test@test.com', password='TestPass123!')
        response = self.client.get(reverse('users:perfil'))
        self.assertEqual(response.status_code, 200)


class EmailOrUsernameBackendTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', email='test@test.com', password='TestPass123!'
        )

    def test_auth_com_email(self):
        from django.contrib.auth import authenticate
        user = authenticate(username='test@test.com', password='TestPass123!')
        self.assertIsNotNone(user)
        self.assertEqual(user.pk, self.user.pk)

    def test_auth_com_username(self):
        from django.contrib.auth import authenticate
        user = authenticate(username='testuser', password='TestPass123!')
        self.assertIsNotNone(user)

    def test_auth_email_case_insensitive(self):
        from django.contrib.auth import authenticate
        user = authenticate(username='TEST@test.com', password='TestPass123!')
        self.assertIsNotNone(user)

    def test_auth_senha_errada(self):
        from django.contrib.auth import authenticate
        user = authenticate(username='test@test.com', password='SenhaErrada')
        self.assertIsNone(user)
