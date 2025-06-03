import pandas as pd

def gerar_estatisticas(nome_arquivo='historico.csv'):
    """
    Gera e exibe estatísticas simples a partir do histórico de medições.
    """
    try:
        df = pd.read_csv(nome_arquivo)
    except FileNotFoundError:
        print(f"\n⚠️ Arquivo '{nome_arquivo}' não encontrado. Nenhum relatório gerado.")
        return

    print("\n=== RELATÓRIOS E ESTATÍSTICAS ===")

    # ✅ Quantidade total de registros
    total_registros = df['registro'].nunique()
    print(f"\nTotal de registros (rodadas): {total_registros}")

    # ✅ Quantidade de medições total
    total_medicoes = len(df)
    print(f"Total de medições no histórico: {total_medicoes}")

    # 1️⃣ Quantidade de registros por nível de risco (geral)
    print("\n1️⃣ Quantidade TOTAL de registros por nível de risco:")
    print(df['risco'].value_counts())

    # 2️⃣ Quantidade de registros por nível de risco POR REGISTRO
    print("\n2️⃣ Quantidade de registros por nível de risco POR REGISTRO:")
    riscos_por_registro = df.groupby(['registro', 'risco']).size().unstack(fill_value=0)
    print(riscos_por_registro)

    # 3️⃣ Nível médio da água por registro
    print("\n3️⃣ Nível médio da água POR REGISTRO:")
    nivel_medio_por_registro = df.groupby('registro')['nivel_agua'].mean()
    print(nivel_medio_por_registro)

    # 4️⃣ Intensidade média da chuva por registro
    print("\n4️⃣ Intensidade média da chuva POR REGISTRO:")
    chuva_media_por_registro = df.groupby('registro')['intensidade_chuva'].mean()
    print(chuva_media_por_registro)

    # 5️⃣ Cidades mais monitoradas (geral)
    print("\n5️⃣ Cidades mais monitoradas (geral):")
    print(df['cidade'].value_counts())

    # 6️⃣ Cidades com maior número de riscos 'Alto' (geral)
    print("\n6️⃣ Cidades com mais ocorrências de Risco ALTO (geral):")
    alto_risco = df[df['risco'] == 'Alto']
    print(alto_risco['cidade'].value_counts())

    print("\n=== FIM DOS RELATÓRIOS ===\n")