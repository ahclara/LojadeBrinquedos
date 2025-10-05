from Produto import Produto
from datetime import datetime
from typing import List, Dict, Optional 

class ItemVenda:
    def __init__(self, produto: Produto, quantidade: int):
        self.produto = produto
        self.quantidade = quantidade
        self.preco = produto.preco_unitario

    def calcular_subtotal(self) -> float:
        subtotal = self.quantidade * self.preco
        return subtotal

    def __str__(self):
        return f"ItemVenda(Produto: {self.produto.nome}, Qtd: {self.quantidade}, Subtotal: R${self.calcular_subtotal():.2f})"
