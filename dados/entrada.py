# dados/entrada.py

def coletar_dados_usuario():
    """
    Solicita os dados do usuário via input e retorna um dicionário com os dados validados.
    Retorna:
        dict: Contendo cidade, nivel_agua, intensidade_chuva, alerta_defesa_civil, etc.
    """
    print("=== Sistema de Monitoramento de Enchentes ===")

    cidade = input("Informe o nome da cidade: ").strip().title()

    while True:
        try:
            nivel_agua = float(input("Nível da água (em metros): "))
            if nivel_agua < 0:
                raise ValueError
            break
        except ValueError:
            print("Valor inválido. Digite um número não negativo.")

    while True:
        try:
            intensidade_chuva = int(input("Intensidade da chuva (0-100): "))
            if 0 <= intensidade_chuva <= 100:
                break
            else:
                raise ValueError
        except ValueError:
            print("Digite um valor entre 0 e 100.")

    while True:
        alerta_defesa_civil = input("Alerta da Defesa Civil? (s/n): ").strip().lower()
        if alerta_defesa_civil in ["s", "n"]:
            break
        else:
            print("Digite 's' para sim ou 'n' para não.")

    return {
        "cidade": cidade,
        "nivel_agua": nivel_agua,
        "intensidade_chuva": intensidade_chuva,
        "alerta_defesa_civil": alerta_defesa_civil == "s"
    }


# Para usar este módulo no main.py:
if __name__ == "__main__":
    from dados.entrada import coletar_dados_usuario
    dados = coletar_dados_usuario()
    print(dados)

