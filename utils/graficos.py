# utils/graficos.py
#GS de Differentiated Problem Solving

import matplotlib.pyplot as plt
import numpy as np

def gerar_grafico_polinomiais(cidade, niveis_rio):
    """
    Gera um gráfico com polinômios baseado na função matemática f(x) = -0.02x³ + 0.35x² - 0.6x + 0.5.
    """
    print("\n=== GERANDO GRÁFICO POLINOMIAL ===")

    dias = np.arange(1, 11)  # Dias de 1 a 10

    # Calcula os níveis com base na função polinomial
    niveis = -0.02 * dias**3 + 0.35 * dias**2 - 0.6 * dias + 0.5

    # Ponto máximo
    dia_maximo = dias[np.argmax(niveis)]
    nivel_maximo = np.max(niveis)

    # Dias de risco (> 2m)
    dias_risco = dias[niveis > 2]
    niveis_risco = niveis[niveis > 2]

    # Plot direto
    plt.figure(figsize=(10, 6))
    plt.plot(dias, niveis, marker='o', linestyle='-', color='blue', linewidth=2, label='Função f(x)')
    plt.scatter(dias_risco, niveis_risco, color='red', label='Dias de risco (>2m)', s=100, zorder=5)
    plt.scatter(dia_maximo, nivel_maximo, color='green', label=f'Máximo ({nivel_maximo:.2f}m no dia {dia_maximo})', s=120, zorder=6)

    plt.title(f'Nível do rio em {cidade} - Gráfico (10 dias de chuva)')
    plt.xlabel('Dia')
    plt.ylabel('Nível do rio (m)')
    plt.xticks(dias)
    plt.ylim(0, max(3.5, nivel_maximo + 0.5))  # margem de segurança
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.tight_layout()
    plt.savefig(f'grafico_polinomial_{cidade.lower().replace(" ", "_")}.png')

    print(f"✅ Gráfico 'grafico_polinomial_{cidade.lower().replace(' ', '_')}.png' gerado.")

    # Análise
    print("\n=== ANÁLISE MATEMÁTICA ===")
    print(f"Domínio da função: dias {dias[0]} a {dias[-1]}")
    print(f"Imagem da função: nível do rio de {np.min(niveis):.2f}m a {np.max(niveis):.2f}m")
    print(f"Máximo: {nivel_maximo:.2f}m no dia {dia_maximo}")
    if len(dias_risco) > 0:
        print(f"Dias de risco (>2m): {dias_risco.tolist()}")
    else:
        print("Nenhum dia com risco (>2m).")
    print("=== FIM DA ANÁLISE ===\n")
