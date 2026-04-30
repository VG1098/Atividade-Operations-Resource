def date_questions():
    """
    Função para realizar perguntas ao usuário e validar as respostas.
    """
    data_atividade = input("Digite a data da atividade (formato DD/MM/AAAA): ")
    while True:
        try:
            dia, mes, ano = map(int, data_atividade.split('/'))
            if 1 <= dia <= 31 and 1 <= mes <= 12 and ano > 0:
                break
            else:
                print("Data inválida. Por favor, tente novamente.")
        except ValueError:
            print("Formato de data inválido. Por favor, use o formato DD/MM/AAAA.")
        data_atividade = input("Digite a data da atividade (formato DD/MM/AAAA): ")
        