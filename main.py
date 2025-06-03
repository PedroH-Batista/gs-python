# main.py
 
from dados.entrada import coletar_dados_usuario
from processamento.logica import avaliar_risco
from interface.saida import exibir_relatorio
from utils.armazenamento import salvar_historico
from utils.relatorios import gerar_estatisticas
from utils.graficos import gerar_grafico_modelo_polinomial
 
def monitoramento_normal():
    # Modo de monitoramento normal
    registros = []
    contador = 0
    TOTAL_MEDICOES = 5  # Você pode ajustar
 
    while contador < TOTAL_MEDICOES:
        print(f"\n--- Medição {contador + 1} de {TOTAL_MEDICOES} ---")
        dados = coletar_dados_usuario()
        registros.append(dados)
        contador += 1
 
    print("\n=== RESUMO DAS MEDIÇÕES ===")
    avaliacoes = []
 
    for registro in registros:
        risco = avaliar_risco(registro)
        avaliacoes.append(risco)
        exibir_relatorio(registro, risco)
 
    salvar_historico(registros, avaliacoes)
    gerar_estatisticas()
    gerar_grafico_modelo_polinomial()
 
def simulacao_10_dias():
    # Modo de simulação do desafio: 10 dias de chuva
    print("\n=== SIMULAÇÃO DE 10 DIAS - DESAFIO DO NÍVEL DO RIO ===")
    cidade = input("Informe o nome da cidade: ").strip().title()
    niveis_rio_10_dias = []
 
    for dia in range(1, 11):
        while True:
            try:
                nivel = float(input(f"Dia {dia} - Nível do rio (em metros, 0 a 3): "))
                if 0 <= nivel <= 3:
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Valor inválido. Digite um número entre 0 e 3.")
 
        niveis_rio_10_dias.append(nivel)
 
    gerar_grafico_modelo_polinomial(cidade, niveis_rio_10_dias)
 
def main():
    while True:
        print("\n=== SISTEMA DE MONITORAMENTO NOAH ===")
        print("1. Monitoramento normal")
        print("2. Simulação de 10 dias (Desafio do nível do rio)")
        print("3. Sair")
 
        opcao = input("Escolha uma opção: ")
 
        if opcao == "1":
            monitoramento_normal()
        elif opcao == "2":
            simulacao_10_dias()
        elif opcao == "3":
            print("Encerrando o sistema. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")
 
if __name__ == "__main__":
    main()