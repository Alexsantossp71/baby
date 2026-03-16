# Relatório Parcial - Projeto Integrador em Computação I

**Curso:** DRP02 - Projeto Integrador em Computação I - Turma 001
**Identificação do Grupo:** PJI110 - A2026S1N1 - Grupo 4
**Polo:** [Preencher o Polo da UNIVESP]
**Orientador:** Fernando Pinto Martinez

## Integrantes
- ALEXANDRE RAMOS DE PAULA (RA: 1700561)
- ANA CLARA BARBOSA NISHIMURA
- CINTHIA DE OLIVEIRA ARAUJO MONTEIRO
- SABRINA DE OLIVEIRA ESCOLASTICO GOMES
- ROSELI GONCALVES DE MIRANDA
- ANDRESSA SANTOS BANDEIRA COSTA
- THEYLON VIANNA SALES
- MARCUS VINICIUS MARTINS

---

## 1. Título do Projeto
**Permutas Baby: Plataforma de Economia Circular para Artigos Infantis**

## 2. Introdução

### 2.1 Contextualização e Justificativa
A chegada de um bebê é um momento de grande alegria e transformação para as famílias. No entanto, é também um período marcado por um alto volume de consumo e acúmulo de bens materiais, tais como fraldas, roupas e acessórios infantis. Devido ao rápido crescimento dos bebês, muitos desses produtos tornam-se obsoletos antes mesmo de serem utilizados em sua capacidade total.

O alto custo de aquisição desses itens, aliado ao desperdício gerado pelo seu não aproveitamento, cria um impacto financeiro significativo para as famílias e um problema ambiental devido ao descarte prematuro. Diante desse cenário, surge a necessidade de fomentar a economia circular entre pais e gestantes, permitindo que produtos em bom estado possam ser trocados e reaproveitados.

### 2.2 O Problema
Identificou-se que as famílias acumulam grandes volumes de itens (especialmente fraldas e roupas) que perdem a utilidade rapidamente. A ausência de uma plataforma digital focada especificamente em conectar famílias para a permuta colaborativa de artigos infantis dificulta o reaproveitamento desses itens de forma fácil, segura e sem transações monetárias diretas, focando no modelo de escambo.

### 2.3 Objetivos
**Objetivo Geral:** 
Desenvolver uma aplicação web (Permutas Baby) com banco de dados para conectar famílias, permitindo a permuta segura e intuitiva de artigos infantis, fomentando a economia circular e colaborativa.

**Objetivos Específicos:**
- Aplicar o *Design Thinking* e processos de *Human-Centered Design* (HCD) para desenhar um fluxo de permuta simplificado;
- Implementar um Banco de Dados relacional para gerenciar usuários, catálogo de produtos e propostas de troca;
- Desenvolver a aplicação utilizando o framework **Django** (Python), integrando Front-end responsivo e Back-end robusto;
- Entregar um Produto Mínimo Viável (MVP) funcional e testável.

---

## 3. Desenvolvimento Iterativo e Processo Projetual

### 3.1 Empatia e Definição
Através de pesquisas com o público-alvo, identificamos que a "perda" de fraldas de tamanhos menores (RN e P) é a dor mais frequente. O escopo do projeto foi definido para focar em itens de alto giro como fraldas e roupas, organizados por categorias e tamanhos específicos.

### 3.2 Ideação e Funcionalidades
A solução concebida, o app **baby**, foca nas seguintes funcionalidades principais:
- **Catálogo com Filtros:** Busca por categoria, tamanho (RN a XG para fraldas; meses/anos para roupas) e condição do item.
- **Sistema de Propostas:** Um fluxo onde um usuário oferece um de seus itens em troca do item desejado de outro usuário.
- **Gestão de Inventário:** Cadastro fácil de itens com upload de múltiplas imagens.
- **Favoritos e Visualizações:** Ferramentas para acompanhamento de itens de interesse.

### 3.3 Prototipação (MVP) e Arquitetura do Sistema
O MVP foi construído com a seguinte stack:
- **Framework:** **Django 5.2**, aproveitando seu sistema de autenticação e ORM para produtividade e segurança.
- **Banco de Dados:** **SQLite** para a fase de prototipagem e desenvolvimento inicial.
- **Front-end:** HTML/CSS/JS com integração de ícones e design responsivo.
- **Deploy:** Configurado para o ambiente **PythonAnywhere**, utilizando **WhiteNoise** para servir arquivos estáticos de forma eficiente.

---

## 4. Fundamentação Teórica

O projeto fundamenta-se nas disciplinas de:
- **Modelagem de Banco de Dados:** Aplicação de normalização para as entidades `Produto`, `Categoria`, `PropostaTroca` e `User`.
- **Desenvolvimento Web:** Uso do padrão **MVC** (ou MVT no Django) para separação de responsabilidades.
- **Engenharia de Software:** Uso de versionamento com **Git/GitHub** e aplicação de requisitos funcionais baseados na experiência do usuário.
- **Economia Circular:** Reuso de materiais para estender a vida útil dos produtos e reduzir o desperdício ambiental.

---

## 5. Considerações Parciais e Próximos Passos

Até a quinzena Q4, o Grupo 4 superou as expectativas iniciais, já possuindo um MVP funcional do app **baby**. O sistema de autenticação, catálogo de produtos e o fluxo básico de propostas de troca já estão implementados e documentados.

**Próximos Passos:**
1.  Refinamento da interface de usuário baseada em testes de usabilidade iniciais;
2.  Melhoria do sistema de notificações internas para novas propostas;
3.  Finalização do guia de testes para a comunidade e coleta de feedbacks;
4.  Preparação do relatório final e vídeo demonstrativo (Q7).

---

## 6. Referências Bibliográficas

- BEZERRA, Eduardo. *Princípios de Análise e Projeto de Sistemas com UML*. 3. ed. Rio de Janeiro: Elsevier, 2015.
- ELMASRI, Ramez; NAVATHE, Shamkant B. *Sistemas de Banco de Dados*. 6. ed. São Paulo: Pearson Addison Wesley, 2011.
- FUNDO ELLEN MACARTHUR. Rumo à economia circular. 2015.
- SOMMERVILLE, Ian. *Engenharia de Software*. 9. ed. São Paulo: Pearson Prentice Hall, 2011.
- Documentação oficial do framework Django (https://docs.djangoproject.com/).
