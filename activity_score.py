def pontuacao_maxima_atividade():
    """Função para validar a pontuação máxima da atividade
    """
    while True:
        try:
            pontuacao = float(input("Por favor, informe a pontuação máxima da atividade (ex: 10.0): ").strip())
            if pontuacao < 0:
                print("A pontuação máxima deve ser um número positivo. Por favor, tente novamente.")
                continue
            return pontuacao
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido para a pontuação máxima.")