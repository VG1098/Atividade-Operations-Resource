def start_activity():
    """
    Função para iniciar a atividade.
    """
    pergunta1 = input("Você deseja iniciar a atividade? (sim/não): ")
    while pergunta1.lower() not in ["sim", "não"]:
        print("Resposta inválida. Por favor, responda com 'sim' ou 'não'.")
        pergunta1 = input("Você deseja iniciar a atividade? (sim/não): ")
    if pergunta1.lower() == "sim":
        print("Ótimo! Vamos começar a atividade.")
    else:
        print("Tudo bem! Você pode iniciar a atividade quando estiver pronto.")
    