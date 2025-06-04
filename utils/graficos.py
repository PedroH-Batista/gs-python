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
    Gera o gráfico solicitado no desafio: função polinomial fixa que modela o nível do rio.
    niveis_rio: lista com 10 valores (nível do rio em cada dia), cada um entre 0 e 3.
    """
    print("\n=== GERANDO GRÁFICO DO DESAFIO ===")

    dias = np.arange(1, len(niveis_rio) + 1)  # Dias 1 a 10
    niveis = np.array(niveis_rio)

    # Definindo a função polinomial fixa
    def f(x):
        return -0.02 * x**3 + 0.35 * x**2 - 0.6 * x + 0.5

    # Aplicando a função aos níveis informados
    niveis_funcao = f(niveis)

    # Normalizar para que o máximo seja 3
    max_original = np.max(niveis_funcao)
    niveis_funcao_norm = (niveis_funcao / max_original) * 3

    # Ponto máximo da função normalizada
    idx_max = np.argmax(niveis_funcao_norm)
    nivel_maximo = niveis_funcao_norm[idx_max]
    dia_maximo = dias[idx_max]

    # Dias de risco: quando valor normalizado > 2
    dias_risco = dias[niveis_funcao_norm > 2]
    niveis_risco = niveis_funcao_norm[niveis_funcao_norm > 2]

    plt.figure(figsize=(10, 6))

    # Linha conectando os pontos em ordem de dias
    plt.plot(dias, niveis_funcao_norm, label='Função polinomial fixa (normalizada)', color='blue', linewidth=2, marker='o')

    # Pontos observados em preto (todos os pontos)
    plt.scatter(dias, niveis_funcao_norm, color='black', s=80, label='Dados observados')

    # Pontos de risco em vermelho (valores normalizados > 2)
    plt.scatter(dias_risco, niveis_risco, color='red', s=100, label='Dias de risco (f(x) > 2)', zorder=5)

    # Ponto máximo em verde
    plt.scatter(dia_maximo, nivel_maximo, color='green', s=120, label=f'Máximo ({nivel_maximo:.2f}m no dia {dia_maximo})', zorder=6)

    plt.title(f'Nível do rio em {cidade} - Modelo Polinomial Fixo')
    plt.xlabel('Dias')
    plt.ylabel('Nível do rio f(x) (m)')
    plt.xlim(1, 10)
    plt.ylim(0, 3)  # Limite fixo do nível do rio entre 0 e 3
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.tight_layout()
    plt.savefig(f'grafico_modelo_{cidade.lower().replace(" ", "_")}.png')
    plt.close()
    print(f"✅ Gráfico 'grafico_modelo_{cidade.lower().replace(' ', '_')}.png' gerado.")

    # Exibir domínio e imagem
    print("\n=== ANÁLISE MATEMÁTICA ===")
    print(f"Domínio da função: entradas informadas pelo usuário: {niveis.tolist()}")
    print(f"Imagem da função normalizada: nível do rio de {np.min(niveis_funcao_norm):.2f}m a {np.max(niveis_funcao_norm):.2f}m")
    print(f"Máximo: {nivel_maximo:.2f}m no dia {dia_maximo}")
    if len(dias_risco) > 0:
        print(f"Dias de risco (f(x) > 2): {dias_risco.tolist()}")
    else:
        print("Nenhum dia com risco (f(x) > 2).")
    print("=== FIM DA ANÁLISE ===\n")
