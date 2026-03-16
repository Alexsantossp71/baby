# Guia Completo: Projeto Integrador em Computação I (UNIVESP)
**Curso:** DRP02 - Projeto Integrador em Computação I - Turma 001

Este documento consolida todas as exigências, cronogramas de entrega, formatos exigidos e stack tecnológico demandados pela disciplina.

---

## 1. Cronograma de Entregas Obrigatórias

O projeto é desenvolvido ao longo do semestre letivo, estruturado em **7 Quinzenas**. Os entregáveis oficiais à universidade concentram-se nas quinzenas Q2, Q4 e Q7.

*Atenção aos formatos: Todos os textos devem ser elaborados a partir dos modelos institucionais disponibilizados pela coordenação no AVA (em formato .docx), porém, **as submissões na plataforma devem ocorrer exclusivamente em formato .PDF**.*

### Resumo das Entregas

| Quinzena | Submissão | Formato Exigido | Prazo Estimado* |
| :--- | :--- | :--- | :--- |
| **Q2** | Plano de Ação | `.PDF` | Consulta no AVA (Ex: ~17/03/2026) |
| **Q4** | Relatório Parcial | `.PDF` | Consulta no AVA (Ex: ~07/04/2026) |
| **Q7** | Relatório Final | `.PDF` | Consulta no AVA (Ex: ~19/05/2026) |
| **Q7** | Vídeo do Projeto | Link (Ficha Técnica) | Consulta no AVA (Ex: ~19/05/2026) |
| **Q7** | Avaliação Colaborativa | `.PDF` | Consulta no AVA (Ex: ~19/05/2026) |

*(Nota: Os prazos exatos devem ser constantemente verificados no calendário oficial do AVA da turma).*

---

## 2. Detalhamento dos Documentos e Estruturas Exigidas

Abaixo estão as especificações do que a banca avaliadora exigirá ler em cada um dos documentos que seu grupo submeterá.

### 2.1. Plano de Ação (Entrega na Quinzena 2)
A pedra fundamental do projeto. Demonstra o planejamento inicial.
*   **Identificação:** Nomes completos e RAs de todos os integrantes do grupo.
*   **Tema/Título:** O título provisório do trabalho de vocês.
*   **O Problema (A Dor):** Definição clara de qual será o problema exato que vocês escolheram resolver na comunidade.
*   **Objetivos:**
    *   *Objetivo Geral:* A meta principal da aplicação.
    *   *Objetivos Específicos:* Os passos menores mensuráveis para atingir a meta.
*   **Cronograma:** Uma tabela/gantt detalhando "quem faz o quê" e "quando fará" ao longo do semestre.

### 2.2. Relatório Parcial (Entrega na Quinzena 4)
O documento de meio de percurso documentando o avanço.
*   **Título Definido:** Síntese final do foco do trabalho.
*   **Introdução:** Contextualização geral inicial do cenário escolhido.
*   **Desenvolvimento Iterativo:**
    *   Como vocês aplicaram a metodologia de *Design Thinking* até chegar à solução prototipada.
    *   Resultados das entrevistas / escuta da comunidade externa.
*   **Fundamentação Teórica:** Referencial bibliográfico que está guiando as escolhas do grupo (livros, tutorias, base científica).

### 2.3. Relatório Final (Entrega na Quinzena 7)
O documento mais extenso, que consolida a disciplina.
*   **Atenção Crítica:** A Capa (ou contra-capa, conforme o template) **deve conter o link público** para o vídeo do projeto.
*   **Resumo Acadêmico.**
*   **Introdução Refinada.**
*   **Metodologia Detalhada:** A explicação passo a passo de como criaram a solução e como as disciplinas ofertadas pela Univesp no Eixo de Computação fundamentaram o trabalho.
*   **Apresentação de Resultados:** Os *prints* e a arquitetura técnica da aplicação web finalizada e testada (o Software MVP entregue).
*   **Considerações Finais:** Lições aprendidas, o que a comunidade achou e sugestões de melhoria (próximos passos).
*   **Referências:** A bibliografia completa no padrão ABNT.

### 2.4. Demonstração / Vídeo do Projeto MVP (Entrega na Quinzena 7)
Trata-se do *pitch* e do teste do software.
*   **Formato Físico de Entrega:** Você **NÃO** faz upload o .mp4 no portal. Vocês preenchem a "Ficha Técnica do Vídeo" e inserem uma URL pública/Não-Listada para um visualizador (YouTube, Google Drive aberto).
*   **Duração:** Padrão sugerido entre 5 a 10 minutos (checar sempre a regra atualizada no modelo).
*   **Conteúdo Obrigatório:**
    *   Apresentar o grupo e qual foi o problema encontrado na comunidade.
    *   Mostrar a solução funcionando (navegar pelo site simulando o uso de um usuário real).

### 2.5. Avaliação Colaborativa (Entrega na Quinzena 7)
*   **Natureza:** Autoavaliação e heteroavaliação.
*   **Objetivo:** Uma reflexão em grupo sobre as facilidades e atritos enfrentados trabalhando em equipe, além do comprometimento de cada integrante.

---

## 3. Requisitos Tecnológicos (Stack Obrigatória)

A banca não aceita "projetos genéricos" nem "redações teóricas" soltas; o grupo é obrigado a desenhar, codificar e colocar no ar uma aplicação nos moldes de desenvolvimento contemporâneo.

1.  **Framework Web:** A aplicação deve obrigatoriamente ser construída em cima de uma biblioteca base. A Univesp fomenta o uso de **Python**, recomendando amplamente **Flask** (para microsserviços e simplicidade) ou **Django** (para robustez "baterias inclusas"). *Outros frameworks podem ser questionados, mas tecnologias como React, Node.js ou Spring podem ser debatidas se o grupo dominar e alinhar via fóruns com os monitores*. No entanto, Python está no cerne da bibliografia sugerida no módulo.
2.  **Persistência de Dados (Banco de Dados):** O sistema não pode ser apenas "HTML estático" (*front-end loose*). Há obrigatoriedade de armazenar, inserir e resgatar dados relacionalmente. É exigido o uso formal de banco de dados (MySQL, PostgreSQL, etc) ou ORMs equivalentes integrados (ex: *SQLAlchemy* no Flask ou ORM padrão do Django).
3.  **Hospedagem / Deploy:** Idealmente o app não deve rodar apenas "no *localhost* do aluno". Espera-se que seja demonstrado "no ar" de alguma forma durante os testes da comunidade (ainda que de forma gratuita via Heroku, Render ou análogos).
4.  **Controle de Versões Escrito (Git):** Não se usa envio de códigos em `.zip`. As equipes precisam obrigatoriamente aplicar versionamento e trabalho colaborativo armazenando o projeto num repositório no **GitHub**, integrando os *commits* entre os alunos.

---

## 4. Metodologias Exigidas na Documentação

Além da tecnologia (o código), as escolhas precisam estar validadas por paradigmas e disciplinas metodológicas cobradas nos Relatórios:

*   **PBL (Problem-Based Learning):** O ponto prepoderante é um problema *externo real* (comunidade visada), e o aprendizado é o esforço focado para resolvê-lo.
*   **HCD (Human-Centered Design) e Design Thinking:** A elaboração não parte do programador, e sim do usuário:
    *   **1. Empatia:** Investigar junto aos alvos suas dores e dificuldades no cotidiano.
    *   **2. Definição:** Pinçar dessas dores e isolar *apenas uma* passível de auxílio tecnológico no semestre.
    *   **3. Ideação:** Propostas para sanar a dor.
    *   **4. Prototipação:** O desenvolvimento da aplicação em si (o Produto Mínimo Viável - MVP).
    *   **5. Testes da Solução:** Entregar este software (WebApp) nas mãos dessa comunidade, aplicar testes, documentar como interagem com a interface e quais são os resultados colhidos. Reflexão e melhoria na Quinzena 6 antes da Entrega na Q7.
