# interface/saida.py

def exibir_relatorio(dados, risco):
    """
    Exibe um relatório formatado com os dados da cidade e o risco avaliado.
    """
    print("\n=== RELATÓRIO DE MONITORAMENTO ===")
    print(f"Cidade monitorada: {dados['cidade']}")
    print(f"Nível da água: {dados['nivel_agua']} m")
    print(f"Intensidade da chuva: {dados['intensidade_chuva']}%")
    print(f"Alerta da Defesa Civil: {'Sim' if dados['alerta_defesa_civil'] else 'Não'}")
    print(f"\nNível de risco: {risco.upper()}")

    if risco == "Alto":
        print("⚠️  Atenção! Risco crítico de enchente. Acione as autoridades locais.")
    elif risco == "Moderado":
        print("🔶 Monitoramento contínuo necessário. Fique atento às atualizações.")
    else:
        print("🟢 Situação estável. Nenhum risco iminente.")
