#!/bin/bash

# Instala as dependências
echo "Instalando dependências..."
python3 -m pip install -r requirements.txt

# Roda as migrations (Cria as tabelas no Neon Postgres)
echo "Rodando migrations..."
python3 manage.py migrate --noinput

# Cria superusuário automaticamente se configurado
echo "Configurando superusuário..."
python3 manage.py setup_admin

# Cria usuários de teste (UserLake1-10 / PassLake123!)
echo "Criando usuários de teste..."
python3 manage.py setup_test_users

# Coleta arquivos estáticos
echo "Coletando arquivos estáticos..."
python3 manage.py collectstatic --noinput --clear

echo "Build concluído com sucesso!"
