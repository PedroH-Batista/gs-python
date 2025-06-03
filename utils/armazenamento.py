import pandas as pd

def salvar_historico(registros, avaliacoes, nome_arquivo='historico.csv'):
    """
    Salva o histórico de medições em um arquivo CSV, acumulando os dados e registrando o número da rodada.
    """
    try:
        # Tenta ler o histórico existente
        df_antigo = pd.read_csv(nome_arquivo)
        # Descobre o maior número de registro já existente
        ultimo_registro = df_antigo['registro'].max()
        novo_registro = ultimo_registro + 1
    except (FileNotFoundError, KeyError):
        # Se não existir histórico, ou não tiver coluna 'registro', começa do 1
        novo_registro = 1

    # Prepara lista de linhas para o DataFrame
    linhas = []
    for dados, risco in zip(registros, avaliacoes):
        linha = {
            'registro': novo_registro,
            'cidade': dados['cidade'],
            'nivel_agua': dados['nivel_agua'],
            'intensidade_chuva': dados['intensidade_chuva'],
            'alerta_defesa_civil': 'Sim' if dados['alerta_defesa_civil'] else 'Não',
            'risco': risco
        }
        linhas.append(linha)

    # Cria DataFrame com os novos registros
    df_novos = pd.DataFrame(linhas)

    try:
        # Se já existia histórico, concatena
        df_antigo = pd.read_csv(nome_arquivo)
        df_total = pd.concat([df_antigo, df_novos], ignore_index=True)
    except FileNotFoundError:
        # Se não existia histórico, só usa os novos registros
        df_total = df_novos

    # Salva no CSV
    df_total.to_csv(nome_arquivo, index=False, encoding='utf-8')
    print(f"\n✅ Histórico atualizado (registro {novo_registro}) salvo em '{nome_arquivo}'.")