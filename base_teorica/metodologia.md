# 4. METODOLOGIA

A metodologia adotada para o desenvolvimento do projeto Permutas Baby baseia-se no framework de *Design Thinking*, dividido em três etapas macro que orientam desde a compreensão do problema até a validação da solução tecnológica.

## 4.1 Ouvir e Interpretar o Contexto

Nesta fase inicial, o grupo buscou compreender a realidade das famílias brasileiras em relação ao consumo de artigos infantis.

*   **Descrição do Contexto:** O projeto foi realizado no ambiente de comunidades digitais de mães e pais, onde se observa um fluxo intenso, porém desorganizado, de doações e trocas de itens.
*   **Perfil dos Participantes:** Famílias com crianças entre 0 e 10 anos, residentes em áreas urbanas, que possuem acesso à internet e buscam alternativas para reduzir gastos com itens de obsolescência rápida (fraldas, roupas e calçados).
*   **Coleta de Informações:** Foram utilizados dois instrumentos principais:
    1.  **Observação Participante:** Acompanhamento de grupos de *Facebook* e *WhatsApp* dedicados ao desapego de itens infantis, identificando dores como a falta de filtros e a insegurança nas transações.
    2.  **Questionário Online:** Aplicação de formulário via *Google Forms* para quantificar o interesse pelo escambo digital e as funcionalidades mais desejadas em uma plataforma específica.

## 4.2 Criar e Prototipar

A partir dos dados coletados, iniciou-se a fase de análise e desenho da solução.

*   **Análise de Dados:** A abordagem foi predominantemente qualitativa, focada na experiência do usuário para definir a jornada de troca. Os dados quantitativos do questionário serviram para priorizar as categorias de produtos mais urgentes (Fraldas e Vestuário).
*   **Soluções Desenvolvidas:** Projetou-se uma plataforma web responsiva utilizando a arquitetura MVT do framework Django. A solução incluiu:
    *   Um catálogo de produtos filtrável por categoria e tamanho;
    *   Um motor de propostas de troca que permite ao usuário ofertar um item do seu inventário em troca de um item de outro usuário;
    *   Um sistema de autenticação para garantir a rastreabilidade dos participantes.

## 4.3 Implementar e Testar

A fase final envolveu o desenvolvimento técnico e a validação do Produto Mínimo Viável (MVP).

*   **Testes da Solução:** O sistema foi submetido a testes alfa realizados pelos próprios integrantes do grupo e, posteriormente, testes beta com um grupo restrito de usuários reais. Os testes focaram na integridade do banco de dados ao processar transações de permuta e na navegabilidade da interface.
*   **Devolutivas e Melhorias:**
    *   **Feedback:** Usuários indicaram que a visualização de fotos dos produtos era o fator decisivo para a confiança na troca.
    *   **Melhorias Implementadas:** Adicionou-se suporte para upload de múltiplas imagens por item e um sistema de notificações simples para alertar sobre novas propostas recebidas.
*   **Resultados Obtidos:** A validação demonstrou que a formalização do escambo através de uma plataforma estruturada reduz significativamente o tempo gasto na negociação em comparação aos métodos informais de redes sociais.
