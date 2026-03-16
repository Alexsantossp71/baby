# 3. FUNDAMENTAÇÃO TEÓRICA

A fundamentação teórica deste trabalho baseia-se nos pilares da economia circular, no consumo colaborativo e nas tecnologias modernas de desenvolvimento web, especificamente o framework Django.

## 3.1 Economia Circular e Consumo Colaborativo

A economia circular propõe uma mudança de paradigma no sistema produtivo, visando dissociar o crescimento econômico do consumo de recursos finitos. De acordo com a Ellen MacArthur Foundation (2015), este modelo baseia-se em três princípios: eliminar resíduos e poluição desde o princípio, manter produtos e materiais em uso e regenerar sistemas naturais.

No contexto de artigos infantis, o consumo colaborativo surge como uma estratégia prática de economia circular. Botsman e Rogers (2011) definem o consumo colaborativo como o compartilhamento, empréstimo, aluguel e troca de bens, permitindo que os indivíduos tenham acesso ao benefício de um produto sem necessariamente detê-lo permanentemente. No Brasil, tais práticas têm ganhado força:

> O consumo colaborativo, cujos pressupostos foram desenvolvidos por Botsman e Rogers (2011), tem sido um tema de crescente interesse em artigos acadêmicos no Brasil, frequentemente explorado em sua relação com a economia circular e a sustentabilidade. (SCIELO, 2021).

O escambo de artigos infantis, como proposto no projeto Permutas Baby, alinha-se a essa visão ao permitir que produtos com vida útil residual sejam redistribuídos, estendendo seu ciclo de vida e reduzindo a necessidade de novas aquisições.

## 3.2 Arquitetura do Sistema e Framework Django

Para a viabilização técnica da plataforma, optou-se pelo uso do framework Django, uma ferramenta de alto nível escrita em Python que incentiva o desenvolvimento rápido e um design limpo e pragmático. A arquitetura central do Django baseia-se no padrão **MVT (Model-View-Template)**.

### 3.2.1 Padrão MVT e ORM

Diferentemente do padrão MVC (Model-View-Controller) tradicional, o Django gerencia a parte do controlador automaticamente, deixando para o desenvolvedor a definição do modelo, da visão e do template (MOZILLA, 2023).

*   **Model:** Representa a estrutura dos dados por meio do Mapeamento Objeto-Relacional (ORM). O ORM permite que o banco de dados seja manipulado como objetos Python, o que "simplifica o acesso aos dados e melhora a legibilidade do código" (ALURA, 2023).
*   **View:** Contém a lógica de negócio que processa as requisições e retorna as respostas adequadas, interagindo com o Model.
*   **Template:** Responsável pela camada de apresentação, utilizando a Django Template Language (DTL) para gerar o HTML dinâmico.

A adoção do princípio **DRY (Don't Repeat Yourself)** no Django é fundamental para a manutenção acadêmica do projeto, pois garante que cada conceito tenha uma única representação no código, reduzindo erros e redundâncias (DJANGOPROJECT, 2024).

### 3.2.2 Bancos de Dados Relacionais

A escolha por bancos de dados relacionais para o gerenciamento de permutas justifica-se pela necessidade de garantir a integridade referencial entre usuários, produtos e propostas. De acordo com Elmasri e Navathe (2011), os sistemas de banco de dados proporcionam uma estrutura eficiente para armazenar volumes crescentes de dados, garantindo que relações complexas — como o vínculo entre uma proposta de troca e dois itens distintos de usuários diferentes — sejam processadas com segurança e consistência.
