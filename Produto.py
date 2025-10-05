from datetime import datetime
from typing import List, Dict, Optional 

class Produto:
    def __init__(self, id_produto: int, nome: str, preco_unitario: float, estoque: int):
        self.id_produto = id_produto    
        self.nome = nome              
        self.preco_unitario = preco_unitario 
        self.estoque = estoque          

    def atualizar_estoque(self, quantidade: int) -> bool:
        if self.estoque + quantidade >= 0:
            self.estoque += quantidade
            print(f"Estoque de '{self.nome}' atualizado. Novo estoque: {self.estoque}")
            return True
        else:
            print(f"Erro: Estoque insuficiente para remover {abs(quantidade)} unidades de '{self.nome}'. Estoque atual: {self.estoque}")
            return False

    def consultar_detalhes(self) -> Dict:
        detalhes = {
            "ID": self.id_produto,
            "Nome": self.nome,
            "Preço Unitário": self.preco_unitario,
            "Estoque": self.estoque
        }
        print(f"Detalhes do Produto: {detalhes}")
        return detalhes

    def __str__(self):
        return f"Produto(ID: {self.id_produto}, Nome: {self.nome}, Preço: R${self.preco_unitario:.2f}, Estoque: {self.estoque})"
