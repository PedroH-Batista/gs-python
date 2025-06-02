# main.py

from dados.entrada import coletar_dados_usuario
from processamento.logica import avaliar_risco
from interface.saida import exibir_relatorio
from utils.armazenamento import salvar_historico

# Lista que vai armazenar os registros 
registros = []

# Controle de medições
contador = 0
TOTAL_MEDICOES = 5  # Você pode mudar este valor

# Coleta dos dados 
while contador < TOTAL_MEDICOES:
    print(f"\n--- Medição {contador + 1} de {TOTAL_MEDICOES} ---")
    
    dados = coletar_dados_usuario()
    
    registros.append(dados)  # Armazena na lista
    
    contador += 1

# Processamento dos registros 
print("\n=== RESUMO DAS MEDIÇÕES ===")
for registro in registros:
    risco = avaliar_risco(registro)
    exibir_relatorio(registro, risco)

# Processamento dos registros
print("\n=== RESUMO DAS MEDIÇÕES ===")
avaliacoes = []  # Nova lista para armazenar os riscos

for registro in registros:
    risco = avaliar_risco(registro)
    avaliacoes.append(risco)  # Guarda o risco
    exibir_relatorio(registro, risco)

# Salva o histórico em CSV
salvar_historico(registros, avaliacoes)