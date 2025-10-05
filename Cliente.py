from datetime import datetime
from typing import List, Dict, Optional 

class Cliente:
    def __init__(self, id_cliente: int, nome: str, cpf: str, email: str):
        self.id_cliente = id_cliente 
        self.nome = nome           
        self.cpf = cpf              
        self.email = email          

    def cadastrar(self) -> None:
        print(f"Cliente '{self.nome}' com ID {self.id_cliente} cadastrado.")
        pass 

    def atualizar_cadastro(self) -> None:
        print(f"Cadastro do cliente '{self.nome}' atualizado.")
        pass 

    def __str__(self):
        return f"Cliente(ID: {self.id_cliente}, Nome: {self.nome}, CPF: {self.cpf})"
