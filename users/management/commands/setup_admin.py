import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Cria um superusuário automaticamente se as variáveis de ambiente existirem'

    def handle(self, *args, **options):
        User = get_user_model()
        username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
        email = os.environ.get('DJANGO_SUPERUSER_EMAIL')
        password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')

        if not username or not email or not password:
            self.stdout.write(self.style.WARNING(
                'Variáveis de ambiente do superusuário não configuradas. Pulando criação.'
            ))
            return

        if not User.objects.filter(username=username).exists():
            self.stdout.write(f'Criando superusuário: {username}')
            User.objects.create_superuser(
                username=username,
                email=email,
                password=password
            )
            self.stdout.write(self.style.SUCCESS(f'Superusuário {username} criado com sucesso!'))
        else:
            self.stdout.write(self.style.NOTICE(f'Superusuário {username} já existe.'))
