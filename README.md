# 🛍️ Sistema Básico de Loja de Brinquedos



# Contexto do Projeto



Este projeto é uma implementação básica de um sistema de vendas e gestão de uma Loja de Brinquedos. Ele se baseia em diagramas UML (Diagrama de Casos de Uso e Diagrama de Classes) para modelar as interações entre os atores e a estrutura de dados do sistema.



O objetivo principal é demonstrar os conceitos de Programação Orientada a Objetos (POO), de Projetos de Software, como classes, atributos, métodos, e diferentes tipos de relacionamentos (associação, composição e dependência), utilizando a linguagem Python.





# 🏗️ Estrutura do Sistema



O sistema foi modelado com as seguintes classes principais para refletir as entidades e processos de uma loja real:



### 1. Classes de Entidades



| Classe | Descrição |

**`Cliente`** - Representa o consumidor que realiza compras. Possui dados cadastrais (nome, CPF, email). 

**`Produto`** - Representa os brinquedos em estoque. Gerencia o nome, preço unitário e a quantidade em `estoque`. 



### 2. Classes de Transação e Processo



| Classe | Descrição | Relacionamentos Chave |

**`ItemVenda`** - Detalha um único produto dentro de uma transação. Fixa o preço e a quantidade vendida. // **Composição** (1..N) com `Venda` 

**`Venda`** - Agrupa os `ItemVenda`s e registra a transação completa. Mantém o `valor_total` e o `status` (pendente, pago). // **Associação** com `Cliente` 

**`ServicoPagamento`** - Simula a integração com uma API externa para processar e estornar pagamentos. // **Dependência (`<<use>>`)** com `Venda` 


---



## ⚙️ Diagrama de Classes - Resumo dos Relacionamentos



| Relacionamento | Classes | Tipo de UML | Descrição no Código |


| Cliente -> Venda | $0..N \leftarrow 1$ | **Associação** | A classe `Venda` referencia um objeto `Cliente`. |

| Venda -> ItemVenda | $1 \rightarrow 1..N$ | **Composição** | A classe `Venda` contém uma lista de objetos `ItemVenda`. |

| ItemVenda -> Produto | $1 \rightarrow 1$ | **Associação** | A classe `ItemVenda` referencia um objeto `Produto` para obter seu preço e nome. |

| Venda $\ll$ utiliza $\gg$ ServicoPagamento | N/A | **Dependência** | A classe `Venda` utiliza (chama métodos de) `ServicoPagamento` para finalizar a transação. |



---



## 🛠️ Tecnologias



**Linguagem de Programação:** Python

* **Ambiente de Desenvolvimento:** VSCode

* **Modelagem:** UML (Diagramas de Casos de Uso e Classes)
