# 5. RESULTADOS PRELIMINARES: SOLUÇÃO INICIAL

Este capítulo detalha os resultados obtidos em cada etapa do desenvolvimento da plataforma **Permutas Baby**, consolidando a primeira versão funcional da solução (MVP - Produto Mínimo Viável).

## 5.1 Resultados da Etapa "Ouvir"

A fase de escuta resultou em um mapeamento detalhado das necessidades dos usuários. O principal resultado foi a definição da **Pirâmide de Necessidades do Escambo Materno**:
1.  **Segurança:** Necessidade de saber com quem se está trocando.
2.  **Facilidade de Busca:** Filtros por tamanho de fraldas e idade da criança.
3.  **Gestão de Propostas:** Um local centralizado para visualizar o que foi oferecido e o que foi recebido.

*Figura 1: Representação visual do Problema x Oportunidade (Placeholder para Storyboard de Contexto)*

## 5.2 Resultados da Etapa "Criar"

O processo de criação resultou na definição da arquitetura técnica e na prototipagem das interfaces.

*   **Modelagem de Dados:** Foi estruturado um banco de dados relacional com entidades que permitem o "Match" de interesses.
*   **Protótipo de Baixa Fidelidade:** Desenvolveu-se um *wireframe* focando na simplicidade, garantindo que pais e mães em rotinas atribuladas consigam cadastrar itens em menos de 1 minuto.

*Figura 2: Fluxograma da Proposta de Permuta (Resultado do mapeamento lógico)*

## 5.3 Resultados da Etapa "Implementar" (Solução Inicial)

A implementação técnica resultou no **MVP Permutas Baby v1.0**. Os principais marcos alcançados foram:

1.  **Módulo de Inventário:** Os usuários conseguem cadastrar itens com foto, descrição e estado de conservação.
2.  **Sistema de Propostas:** A funcionalidade principal que permite "ofertar" um item do seu inventário por um item de outro usuário, criando um vínculo lógico de permuta pura.
3.  **Painel de Controle:** Uma visão administrativa onde o usuário acompanha o status das trocas (Pendente, Aceita, Recusada).

### 5.3.1 Demonstração Visual da Solução Real

Abaixo, apresentam-se as capturas de tela da solução real em funcionamento, demonstrando a interface final e as funcionalidades de busca e troca:

![Página Inicial Real - Permutas Baby](file:///C:/Users/arpt1/.gemini/antigravity/brain/593d38a4-505d-4ccc-84b9-6da90c41da3a/permutas_baby_gallery_real_1773676799163.png)
*Figura 3: Interface real do catálogo de produtos com imagens realistas de alta qualidade.*

![Detalhe do Produto e Troca - Permutas Baby](file:///C:/Users/arpt1/.gemini/antigravity/brain/593d38a4-505d-4ccc-84b9-6da90c41da3a/permutas_baby_product_detail_real_1773676832509.png)
*Figura 4: Detalhe do item evidenciando as novas imagens e interface polida.*

*   **Tela Inicial:** Exibe os itens mais recentes postados na comunidade, organizados por proximidade ou categoria.
*   **Detalhe do Produto:** Informações detalhadas sobre o item desejado e o perfil (reputação) do ofertante.
*   **Fluxo de Troca:** O usuário clica em "Propor Troca", seleciona um dos seus próprios itens para oferecer de volta e envia a notificação.

## 5.4 Devolutivas e Evolução

Com base nos primeiros testes de implementação, verificou-se que a solução inicial resolve o problema da desorganização das redes sociais. A principal evolução detectada para o próximo ciclo foi a inclusão de um chat interno para facilitar o agendamento da entrega física dos itens trocados.
