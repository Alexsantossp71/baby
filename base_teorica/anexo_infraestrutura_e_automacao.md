# Anexo: Infraestrutura, Automação e Qualidade - Projeto Baby Lake

Este anexo documenta os aspectos de implantação (DevOps), automação de dados e a validação técnica do sistema através de testes automatizados.

---

## 1. Configuração de Nuvem e Deploy

### 1.1 vercel.json
*Configuração de roteamento e integração com a plataforma Vercel para hospedagem Serverless.*

```json
{
  "version": 2,
  "rewrites": [
    {
      "source": "/static/(.*)",
      "destination": "/static/$1"
    },
    {
      "source": "/(.*)",
      "destination": "permutas_site/wsgi.py"
    }
  ]
}
```

### 1.2 build.sh
*Script de automação para preparação do ambiente em ambiente de produção (CI/CD).*

```bash
#!/bin/bash

# Instala as dependências
echo "Instalando dependências..."
python3 -m pip install -r requirements.txt

# Roda as migrations (Cria as tabelas no banco de dados)
echo "Rodando migrations..."
python3 manage.py migrate --noinput

# Coleta arquivos estáticos
echo "Coletando arquivos estáticos..."
python3 manage.py collectstatic --noinput --clear

echo "Build concluído com sucesso!"
```

### 1.3 requirements.txt
*Lista de dependências e bibliotecas essenciais para o funcionamento do ecossistema Django.*

```text
django==5.2a1
whitenoise>=6.0.0
gunicorn>=21.0.0
psycopg2-binary>=2.9.0
python-dotenv>=1.0.0
Pillow>=10.0.0
django-ratelimit>=4.1.0
dj-database-url>=2.1.0
django-storages>=1.14.0
vercel-blob>=0.4.2
requests>=2.31.0
```

---

## 2. Scripts de Automação de Dados

### 2.1 bulk_update_images.py
*Script utilitário desenvolvido para processar e vincular imagens de forma massiva, garantindo a integridade da vitrine durante a carga inicial.*

```python
import os
import shutil
from baby.models import Produto

def bulk_update_images():
    media_root = r'f:\projetos_opencode\PI2016Django\media\produtos'
    image_map = {
        'ROUPA': 'baby_clothing_boy.png',
        'BRINQUEDO': 'baby_toys.png',
        'MOVEIS': 'baby_crib.png',
        'ALIMENTACAO': 'baby_high_chair.png'
    }
    
    produtos = Produto.objects.all()
    for p in produtos:
        titulo = p.titulo.upper()
        # Lógica de categorização automática baseada em palavras-chave
        if 'ROUPA' in titulo:
            target = image_map['ROUPA']
        # ... (lógica simplificada para o anexo)
        p.imagem_principal = f"produtos/{target}"
        p.save()

if __name__ == "__main__":
    bulk_update_images()
```

---

## 3. Validação e Qualidade de Software

### 3.1 Relatório de Testes Automatizados
O sistema foi submetido a uma bateria de testes unitários e de integração, cobrindo os fluxos críticos de:
- Autenticação de Usuário.
- Cadastro e Edição de Produtos.
- Lógica de Proposta de Troca (Aceite/Rejeição).
- Regras de Negócio e Permissões.

**Resultado da Execução:**
```text
Found 16 test(s).
Creating test database for alias 'default'...
................
----------------------------------------------------------------------
Ran 16 tests in 9.936s

OK
Destroying test database for alias 'default'...
System check identified no issues (0 silenced).
```
**Status Final: APROVADO** (100% de cobertura nos fluxos testados).
