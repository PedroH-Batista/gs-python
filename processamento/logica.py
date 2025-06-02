# processamento/logica.py

def avaliar_risco(dados):
    """
    Recebe um dicionário com os dados da cidade e retorna uma string
    indicando o nível de risco: 'Baixo', 'Moderado' ou 'Alto'.
    """
    nivel = dados["nivel_agua"]
    chuva = dados["intensidade_chuva"]
    alerta = dados["alerta_defesa_civil"]

    if nivel >= 2.0 or chuva > 80 or alerta:
        return "Alto"
    elif nivel >= 1.0 or chuva > 50:
        return "Moderado"
    else:
        return "Baixo"
