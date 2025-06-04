#João Felipe Bertini RM563478
#Luan Durbano Almeida RM563478
#Pedro Batista RM563220

# main.py
 
from dados.entrada import coletar_dados_usuario
from processamento.logica import avaliar_risco
from interface.saida import exibir_relatorio
from utils.armazenamento import salvar_historico
from utils.relatorios import gerar_estatisticas
from utils.graficos import gerar_graficos, gerar_grafico_modelo_polinomial
 
def monitoramento_normal():
    # Modo de monitoramento normal
    registros = []
    contador = 0
    TOTAL_MEDICOES = 2  # Você pode ajustar
 
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
    gerar_graficos()
 
def simulacao_10_dias():
    """
    Função que solicita ao usuário os valores de 1 até 10,
    e os envia para a função polinomial que gera o gráfico baseado na equação matemática.
    """
    print("\n=== MONITORAMENTO DO NÍVEL DO RIO ===")
    print("Digite 10 valores de 1 até 10 (correspondentes a cada dia):")

    dias_rio = []  # Lista para armazenar os dias inseridos pelo usuário
    
    for i in range(10):
        while True:
            try:
                dia = int(input(f"Dia {i+1}: "))  # Solicita um número entre 1 e 10
                if 1 <= dia <= 10 and dia not in dias_rio:  # Garante valores únicos dentro do intervalo
                    dias_rio.append(dia)
                    break
                else:
                    print("⚠️ Insira um número entre 1 e 10, sem repetir!")
            except ValueError:
                print("❌ Entrada inválida! Digite um número inteiro.")

    # Solicita o nome da cidade para inclusão no gráfico
    cidade = input("\n🌍 Informe a cidade onde o monitoramento está sendo feito: ").strip()

    # Chama a função para gerar o gráfico
    gerar_grafico_modelo_polinomial(cidade, dias_rio)
 
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