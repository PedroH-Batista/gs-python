# utils/graficos.py
# Matéria de Differentiated Problem Solving

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from numpy.polynomial.polynomial import Polynomial
 
# Função Baseada no CSV
def gerar_graficos(nome_arquivo='historico.csv'):
    # Tenta ler o arquivo CSV; se não encontrar, exibe uma mensagem e encerra a função
    try:
        df = pd.read_csv(nome_arquivo)
    except FileNotFoundError:
        print(f"\n⚠️ Arquivo '{nome_arquivo}' não encontrado. Nenhum gráfico gerado.")
        return

    # Verifica se todas as colunas necessárias estão presentes no DataFrame
    colunas_necessarias = {'registro', 'risco', 'nivel_agua', 'intensidade_chuva'}
    if not colunas_necessarias.issubset(df.columns):
        print(f"\n⚠️ O arquivo '{nome_arquivo}' não possui as colunas necessárias: {colunas_necessarias}")
        return

    # Converte as colunas 'nivel_agua' e 'intensidade_chuva' para tipo numérico, tratando erros como NaN
    df['nivel_agua'] = pd.to_numeric(df['nivel_agua'], errors='coerce')
    df['intensidade_chuva'] = pd.to_numeric(df['intensidade_chuva'], errors='coerce')

    print("\n=== GERANDO GRÁFICOS DO HISTÓRICO ===")

    # Gera gráfico de barras: quantidade de riscos por registro
    riscos_por_registro = df.groupby(['registro', 'risco']).size().unstack(fill_value=0)
    riscos_por_registro.plot(kind='bar', figsize=(8, 6))
    plt.title('Quantidade de riscos por registro')
    plt.xlabel('Registro')
    plt.ylabel('Quantidade')
    plt.legend(title='Risco')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig('grafico_riscos_por_registro.png')
    plt.close()
    print("✅ Gráfico 'grafico_riscos_por_registro.png' gerado.")

    # Gera gráfico de linha: nível médio da água por registro
    nivel_medio = df.groupby('registro')['nivel_agua'].mean().sort_index()
    plt.figure(figsize=(8, 6))
    plt.plot(nivel_medio.index, nivel_medio.values, marker='o', color='blue')
    plt.title('Nível médio da água por registro')
    plt.xlabel('Registro')
    plt.ylabel('Nível da água (m)')
    plt.xticks(nivel_medio.index)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig('grafico_nivel_agua.png')
    plt.close()
    print("✅ Gráfico 'grafico_nivel_agua.png' gerado.")

    # Gera gráfico de linha: intensidade média da chuva por registro
    chuva_medio = df.groupby('registro')['intensidade_chuva'].mean().sort_index()
    plt.figure(figsize=(8, 6))
    plt.plot(chuva_medio.index, chuva_medio.values, marker='o', color='orange')
    plt.title('Intensidade média da chuva por registro')
    plt.xlabel('Registro')
    plt.ylabel('Intensidade da chuva (%)')
    plt.xticks(chuva_medio.index)
    plt.ylim(0, 100)  # Define o limite do eixo Y entre 0 e 100%
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig('grafico_intensidade_chuva.png')
    plt.close()
    print("✅ Gráfico 'grafico_intensidade_chuva.png' gerado.")

    print("\n=== FIM DOS GRÁFICOS DO HISTÓRICO ===\n")

 

#Para a GS de Differentiated Problem Solving
def gerar_grafico_modelo_polinomial(cidade, niveis_rio):
    """
    Gera o gráfico solicitado no desafio: função polinomial que modela o nível do rio.
    niveis_rio: lista com 10 valores (nível do rio em cada dia).
    """
    print("\n=== GERANDO GRÁFICO DO DESAFIO ===")
 
    dias = np.arange(1, len(niveis_rio) + 1)  # Dias 1 a 10
    niveis = np.array(niveis_rio)
 
    # Ajuste polinomial (grau 3 recomendado para suavização)
    grau = 3
    coeficientes = np.polyfit(dias, niveis, grau)
    p = np.poly1d(coeficientes)
 
    # Domínio: dias 1 a 10 (interpolado para suavizar curva)
    dias_interpolado = np.linspace(1, 10, 100)
    niveis_interpolado = p(dias_interpolado)
 
    # Ponto máximo
    dia_maximo = dias_interpolado[np.argmax(niveis_interpolado)]
    nivel_maximo = np.max(niveis_interpolado)
 
    # Dias de risco (> 2m)
    dias_risco = dias[niveis > 2]
    niveis_risco = niveis[niveis > 2]
 
    # Plot
    plt.figure(figsize=(10, 6))
    plt.plot(dias_interpolado, niveis_interpolado, label=f'Função polinomial (grau {grau})', color='blue', linewidth=2)
    plt.scatter(dias, niveis, color='black', label='Dados observados', s=80)
    plt.scatter(dias_risco, niveis_risco, color='red', label='Dias de risco (>2m)', zorder=5, s=100)
    plt.scatter(dia_maximo, nivel_maximo, color='green', label=f'Máximo ({nivel_maximo:.2f}m no dia {dia_maximo:.0f})', zorder=6, s=120)
 
    plt.title(f'Nível do rio em {cidade} - Modelo Polinomial (10 dias de chuva)')
    plt.xlabel('Dia')
    plt.ylabel('Nível do rio (m)')
    plt.xticks(np.arange(1, 11))
    plt.ylim(0, max(3.5, nivel_maximo + 0.5))  # margem de segurança
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.tight_layout()
    plt.savefig(f'grafico_modelo_{cidade.lower().replace(" ", "_")}.png')
    print(f"✅ Gráfico 'grafico_modelo_{cidade.lower().replace(' ', '_')}.png' gerado.")
 
    # Exibir domínio e imagem
    print("\n=== ANÁLISE MATEMÁTICA ===")
    print(f"Domínio da função: dias 1 a 10")
    print(f"Imagem da função: nível do rio de {np.min(niveis_interpolado):.2f}m a {np.max(niveis_interpolado):.2f}m")
    print(f"Máximo: {nivel_maximo:.2f}m no dia {dia_maximo:.0f}")
    if len(dias_risco) > 0:
        print(f"Dias de risco (>2m): {dias_risco.tolist()}")
    else:
        print("Nenhum dia com risco (>2m).")
    print("=== FIM DA ANÁLISE ===\n")