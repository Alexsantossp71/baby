from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


TEST_USERS = [
    {'username': 'UserLake1', 'email': 'userlake1@example.com'},
    {'username': 'UserLake2', 'email': 'userlake2@example.com'},
    {'username': 'UserLake3', 'email': 'userlake3@example.com'},
    {'username': 'UserLake4', 'email': 'userlake4@example.com'},
    {'username': 'UserLake5', 'email': 'userlake5@example.com'},
    {'username': 'UserLake6', 'email': 'userlake6@example.com'},
    {'username': 'UserLake7', 'email': 'userlake7@example.com'},
    {'username': 'UserLake8', 'email': 'userlake8@example.com'},
    {'username': 'UserLake9', 'email': 'userlake9@example.com'},
    {'username': 'UserLake10', 'email': 'userlake10@example.com'},
]

TEST_PASSWORD = 'PassLake123!'


class Command(BaseCommand):
    help = 'Cria os usuários de teste (UserLake1-10) caso não existam'

    def handle(self, *args, **options):
        User = get_user_model()
        created_count = 0
        skipped_count = 0

        for user_data in TEST_USERS:
            username = user_data['username']
            email = user_data['email']

            if not User.objects.filter(username__iexact=username).exists():
                user = User(username=username, email=email, is_active=True)
                user.set_password(TEST_PASSWORD)
                user.save()
                self.stdout.write(self.style.SUCCESS(f'Criado: {username} ({email})'))
                created_count += 1
            else:
                self.stdout.write(self.style.NOTICE(f'Já existe: {username}'))
                skipped_count += 1

        self.stdout.write(
            self.style.SUCCESS(
                f'\nConcluído: {created_count} criados, {skipped_count} já existentes.'
            )
        )
