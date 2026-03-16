# Guia de Deploy - PythonAnywhere

## Passo 1: Preparar o Código

1. No seu computador, verifique se tudo está funcionando:
```bash
python manage.py check
python manage.py migrate
python manage.py collectstatic
```

2. Crie um arquivo `.gitignore` se não existir:
```
__pycache__/
*.pyc
*.pyo
venv/
.env
*.sqlite3
media/
staticfiles/
```

3. Compacte os arquivos do projeto (exceto venv, .git, etc.)


## Passo 2: Configurar PythonAnywhere

### Acesse: https://www.pythonanywhere.com/user/PI2016G4/

### Aba "Files"
1. Faça upload do arquivo compactado
2. Extraia na pasta `/home/PI2016G4/PI2016Django/`

### Aba "Consoles" - Criar novo Bash console

1. Criar virtualenv (opcional):
```bash
mkvirtualenv --python=python3.11 myenv
workon myenv
```

2. Ir para a pasta do projeto:
```bash
cd /home/PI2016G4/PI2016Django
```

3. Instalar dependências:
```bash
pip install -r requirements.txt
```

### Passo 3: Configurar Web App

1. Vá na aba **"Web"**
2. Clique em **"Add a new web app"**
3. Escolha **"Manual configuration"**
4. Selecione **"Python 3.11"** (ou versão disponível)

### Passo 4: Editar WSGI

1. Clique no link do arquivo WSGI
2. Substitua o conteúdo com:

```python
import os
import sys

# Path to your project
path = '/home/PI2016G4/PI2016Django'
if path not in sys.path:
    sys.path.append(path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'permutas_site.settings')

# For Django >= 3.2
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

3. Salve e volte para a página Web

### Passo 5: Configurar Virtualenv

1. No campo "Virtualenv", digite:
```
/home/PI2016G4/.virtualenvs/myenv
```
(ou o nome que você criou)

### Passo 6: Configurar Arquivos Estáticos

No campo "Static files", adicione:

| URL | Directory |
|-----|-----------|
| /static/ | /home/PI2016G4/PI2016Django/static/ |
| /media/ | /home/PI2016G4/PI2016Django/media/ |

### Passo 7: Configurar Banco de Dados

No console:
```bash
cd /home/PI2016G4/PI2016Django
python manage.py migrate
python manage.py createsuperuser  # opcional
python manage.py collectstatic
```

### Passo 8: Atualizar ALLOWED_HOSTS

Edite o arquivo `permutas_site/settings.py`:

```python
ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'PI2016G4.pythonanywhere.com']
```

### Passo 9: Recarregar

1. Volte para a aba **"Web"**
2. Clique em **"Reload"** botão verde

## URLs do Site

- Site: `https://PI2016G4.pythonanywhere.com`
- Admin: `https://PI2016G4.pythonanywhere.com/admin/`

## Problemas Comuns

### Erro 500 (Internal Server Error)
- Verifique o log de erros na aba Web
- Execute `python manage.py check --deploy` localmente

### Banco de dados SQLite
- O SQLite já vem incluso no PythonAnywhere (plano gratuito)
- Para PostgreSQL, precisa de plano pago

### Arquivos de mídia
- Certifique-se de configurar o WhiteNoise ou usar a configuração de static files

## Configuração Recomendada do settings.py

Para produção, altere:
```python
DEBUG = False
ALLOWED_HOSTS = ['seu-usuario.pythonanywhere.com']

# Para servir arquivos estáticos com WhiteNoise:
MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # ... outros middleware
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```
