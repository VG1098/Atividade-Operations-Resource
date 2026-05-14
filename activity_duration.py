def activity_duration():
    """
    Função para validar a duração da atividade.
    """
    duracao = input("Por favor, informe a duração da atividade em horas (ex: 1): ")
    while not duracao.isdigit() or int(duracao) <= 0:
        print("Duração inválida. Por favor, insira um número inteiro positivo.")
        duracao = input("Por favor, informe a duração da atividade em horas (ex: 1): ")
    print(f"Ótimo! A duração da atividade é de {duracao} horas.")
    return int(duracao)