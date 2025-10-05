from Cliente import Cliente
from ItemVenda import ItemVenda
from ServicoPagamento import ServicoPagamento
from Produto import Produto
from Venda import Venda

print("--- Inicializando o Sistema ---")

servico_api = ServicoPagamento(
    url_api="https://api.pagamentos.com/v1",
    token_autenticacao="abc123xyz"
)

cliente1 = Cliente(
    id_cliente=1,
    nome="Maria Silva",
    cpf="123.456.789-00",
    email="maria@exemplo.com"
)
cliente1.cadastrar()

produto_bola = Produto(id_produto=101, nome="Bola de Futebol", preco_unitario=50.00, estoque=20)
produto_boneca = Produto(id_produto=102, nome="Boneca Mágica", preco_unitario=120.50, estoque=5)

print("\n--- Detalhes dos Produtos Antes da Venda ---")
produto_bola.consultar_detalhes()
produto_boneca.consultar_detalhes()


venda1 = Venda(id_pedido=1001, cliente=cliente1, servico_pagamento=servico_api)


venda1.adicionar_item(produto=produto_bola, quantidade=2)
venda1.adicionar_item(produto=produto_boneca, quantidade=1)

venda1.calcular_total()

dados_cartao = {"numero": "4111...", "cvv": "123"}
venda1.finalizar_venda(dados_cartao)

print("\n--- Resultado Final ---")
print(venda1)

print("\n--- Detalhes dos Produtos Depois da Venda ---")
produto_bola.consultar_detalhes()
produto_boneca.consultar_detalhes()