from datetime import datetime
from typing import List, Dict, Optional 

class ServicoPagamento:
    def __init__(self, url_api: str, token_autenticacao: str):
        self.url_api = url_api                
        self.token_autenticacao = token_autenticacao

    def processar_pagamento(self, valor: float, dados_cartao: Dict) -> Optional[str]:
        print(f"Conectando à API: {self.url_api} para processar R${valor:.2f}...")
        # Simulação de processamento bem-sucedido
        if valor > 0:
            id_transacao = f"TRANS_{datetime.now().strftime('%Y%m%d%H%M%S')}"
            print(f"Pagamento processado com sucesso. ID Transação: {id_transacao}")
            return id_transacao  # String (idTransacao)
        else:
            print("Erro ao processar pagamento: Valor inválido.")
            return None # bool (false)

    def estornar_pagamento(self, id_transacao: str) -> bool:
        print(f"Solicitando estorno para a transação: {id_transacao}...")
        # Simulação de estorno
        if id_transacao.startswith("TRANS_"):
            print("Estorno realizado com sucesso.")
            return True # bool
        else:
            print("Erro: ID de transação inválido ou não encontrado.")
            return False # bool