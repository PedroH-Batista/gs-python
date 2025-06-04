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
def gerar_grafico_modelo_polinomial(cidade, dias_rio):
    """
    Gera o gráfico baseado na função polinomial fixa.
    Substitui os valores inseridos pelo usuário na equação matemática e plota o gráfico corretamente.
    """
    print("\n=== GERANDO GRÁFICO DO DESAFIO ===")

    # Convertendo lista para array NumPy
    dias = np.array(dias_rio)

    # Definição da função polinomial
    def f(x):
        return -0.05 * x**2 + 0.7 * x + 0.2  # Modelo matemático da variação do nível do rio

    # Calcula os valores da função para os números inseridos pelo usuário
    niveis_funcao = f(dias)

    # Identifica o nível máximo
    idx_max = np.argmax(niveis_funcao)
    nivel_maximo = niveis_funcao[idx_max]
    dia_maximo = dias[idx_max]

    # Identifica os dias de risco (>2m)
    dias_risco = dias[niveis_funcao > 2]
    niveis_risco = niveis_funcao[niveis_funcao > 2]

    # Criando o gráfico
    plt.figure(figsize=(10, 6))

    # Linha conectando os pontos em ordem crescente de dias
    plt.plot(dias, niveis_funcao, label='Modelo Polinomial', color='blue', linewidth=2, marker='o')

    # Pontos de risco em vermelho
    plt.scatter(dias_risco, niveis_risco, color='red', s=100, label='Dias de risco (>2m)', zorder=5)

    # Ponto máximo em verde
    plt.scatter(dia_maximo, nivel_maximo, color='green', s=120, label=f'Máximo ({nivel_maximo:.2f}m no dia {dia_maximo})', zorder=6)

    plt.title(f'Nível do rio em {cidade} - Modelo Polinomial')
    plt.xlabel("Dias")
    plt.ylabel("Nível do rio (m)")
    plt.xlim(1, 10)  # Mantém os limites do gráfico fixos
    plt.ylim(0, np.max(niveis_funcao) + 0.5)  # Ajusta a altura do gráfico
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.tight_layout()
    plt.savefig(f'grafico_modelo_{cidade.lower().replace(" ", "_")}.png')
    plt.close()
    print(f"✅ Gráfico 'grafico_modelo_{cidade.lower().replace(' ', '_')}.png' gerado.")

    # Exibir análise matemática
    print("\n=== ANÁLISE MATEMÁTICA ===")
    print(f"Domínio da função: dias inseridos pelo usuário: {dias.tolist()}")
    print(f"Imagem da função: nível do rio variando de {np.min(niveis_funcao):.2f}m a {np.max(niveis_funcao):.2f}m")
    print(f"Máximo: {nivel_maximo:.2f}m no dia {dia_maximo}")
    if len(dias_risco) > 0:
        print(f"Dias de risco (>2m): {dias_risco.tolist()}")
    else:
        print("Nenhum dia de risco detectado.")
    print("=== FIM DA ANÁLISE ===\n")