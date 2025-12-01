# 🛍️ Sistema Básico de Loja de Brinquedos 🧱

## 📜 Contexto e Objetivo do Projeto

Este projeto é uma implementação básica de um sistema de vendas e gestão de uma Loja de Brinquedos. Ele se baseia em **diagramas UML (Diagrama de Casos de Uso e Diagrama de Classes)** para modelar as interações entre os atores e a estrutura de dados do sistema.

O objetivo principal é demonstrar os conceitos de **Programação Orientada a Objetos (POO)** e de **Modelagem de Software**, incluindo classes, atributos, métodos e diferentes tipos de relacionamentos (associação, composição e dependência), utilizando a linguagem Python.

---

## 🏗️ Estrutura do Sistema (Organização de Pacotes)

O código foi estruturado seguindo o padrão MVC (Model-View-Controller) simplificado, agrupando as classes de acordo com suas responsabilidades:

### 1. Pacote `model` (Entidades de Domínio)

Estas classes representam os dados e as regras de negócio fundamentais.

| Classe | Descrição |
| :--- | :--- |
| **`Cliente`** | Representa o consumidor. Possui dados cadastrais (`nome`, `cpf`, `email`). |
| **`Produto`** | Representa os brinquedos em estoque. Gerencia `nome`, `preco_unitario` e a `estoque`. |
| **`ItemVenda`** | Detalha um único produto dentro de uma transação. Fixa o preço e a quantidade vendida. |
| **`Venda`** | Agrupa os `ItemVenda`s e registra a transação completa. Mantém o `valor_total` e o `status`. |

### 2. Pacote `controller` (Controle e Serviços)

Estas classes gerenciam a lógica de aplicação e orquestram as operações.

| Classe | Descrição | Relacionamentos Chave |
| :--- | :--- | :--- |
| **`ServicoPagamento`** | Simula a integração com uma API externa para processar e estornar pagamentos. | **Dependência (`<<use>>`)** com `Venda` |
| **`SistemaVendas`** | Controlador principal que gerencia o fluxo de cadastro e interação entre as entidades. | **Associação** com as entidades do `model` |

### 3. Diagrama de Classes - Resumo dos Relacionamentos

| Relacionamento | Classes | Tipo de UML | Descrição no Código |
| :--- | :--- | :--- | :--- |
| Cliente $\rightarrow$ Venda | $0..N \leftarrow 1$ | **Associação** | A classe `Venda` referencia um objeto `Cliente`. |
| Venda $\rightarrow$ ItemVenda | $1 \rightarrow 1..N$ | **Composição** | A classe `Venda` contém uma lista de objetos `ItemVenda`. |
| ItemVenda $\rightarrow$ Produto | $1 \rightarrow 1$ | **Associação** | A classe `ItemVenda` referencia um objeto `Produto` para obter seu preço e nome. |
| Venda $\ll$ utiliza $\gg$ ServicoPagamento | N/A | **Dependência** | A classe `Venda` utiliza (chama métodos de) `ServicoPagamento` para finalizar a transação. |

---

## ⚙️ Modelo de Persistência (Modelo Relacional)

O modelo relacional abaixo define a estrutura de banco de dados (BD) que seria usada para persistir as informações, seguindo a estrutura lógica do Diagrama de Classes.

| Tabela | Colunas (Chave Primária: **PK**, Chave Estrangeira: *FK*) | Relacionamentos (1:N) |
| :--- | :--- | :--- |
| **CLIENTE** | **id\_cliente (PK)**, nome, cpf, email | **(1)** CLIENTE $\rightarrow$ VENDA |
| **PRODUTO** | **id\_produto (PK)**, nome, preco\_unitario, estoque | **(3)** PRODUTO $\rightarrow$ ITEM\_VENDA |
| **VENDA** | **id\_pedido (PK)**, data\_hora, valor\_total, status, **id\_cliente (\*FK\*)** | **(2)** VENDA $\rightarrow$ ITEM\_VENDA |
| **ITEM\_VENDA** | **id\_venda (PK, \*FK\*)**, **id\_produto (PK, \*FK\*)**, quantidade, preco | **Chave Composta:** id\_venda, id\_produto |
| **PAGAMENTO** | **id_pagamento (PK)**, id_transacao_api, status, **id_venda (*FK*)** | **(1:1)** VENDA $\leftrightarrow$ PAGAMENTO |

---

## 🛠️ Tecnologias e Execução

### Tecnologias Utilizadas
* **Linguagem de Programação:** Python (versão 3.8+)
* **Ambiente de Desenvolvimento:** VSCode
* **Modelagem:** UML (Diagramas de Casos de Uso e Classes)

### 🚀 Instruções de Execução
Para rodar o sistema, siga os passos abaixo:

1.  **Pré-requisitos:** Certifique-se de ter o Python 3 instalado em sua máquina.
2.  **Executar o arquivo principal:**
    ```bash
    python Principal.py
    ```
3.  **Uso:** O sistema irá iniciar no Menu Principal, onde é possível selecionar o perfil de acesso (`1. Cliente`, `2. Vendedor`, `3. Gerente`) para interagir com as funcionalidades modeladas.
