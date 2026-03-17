#!/bin/bash

# Instala as dependências
echo "Instalando dependências..."
python3.12 -m pip install -r requirements.txt

# Roda as migrations (Cria as tabelas no Neon Postgres)
echo "Rodando migrations..."
python3.12 manage.py migrate --noinput

# Coleta arquivos estáticos
echo "Coletando arquivos estáticos..."
python3.12 manage.py collectstatic --noinput --clear

echo "Build concluído com sucesso!"
