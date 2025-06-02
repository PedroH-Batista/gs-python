# utils/armazenamento.py

import pandas as pd

def salvar_historico(registros, avaliacoes, nome_arquivo='historico.csv'):
    """
    Salva o histórico de medições em um arquivo CSV.
    registros: lista de dicionários de medições.
    avaliacoes: lista com os riscos correspondentes a cada medição.
    """
    # Prepara lista de linhas para o DataFrame
    linhas = []
    for dados, risco in zip(registros, avaliacoes):
        linha = {
            'cidade': dados['cidade'],
            'nivel_agua': dados['nivel_agua'],
            'intensidade_chuva': dados['intensidade_chuva'],
            'alerta_defesa_civil': 'Sim' if dados['alerta_defesa_civil'] else 'Não',
            'risco': risco
        }
        linhas.append(linha)

    # Cria o DataFrame e salva no CSV
    df = pd.DataFrame(linhas)
    df.to_csv(nome_arquivo, index=False, encoding='utf-8')
    print(f"\n✅ Histórico salvo em '{nome_arquivo}'.")
