def deliver_activity():
    """
    Função para entregar a atividade, permitindo colar o código usado.
    """
    pergunta1 = input("Você deseja entregar a atividade? (sim/não): ")
    while pergunta1.lower() not in ["sim", "não"]:
        print("Resposta inválida. Por favor, responda com 'sim' ou 'não'.")
        pergunta1 = input("Você deseja entregar a atividade? (sim/não): ")
    if pergunta1.lower() == "sim":
        print("Cole abaixo o código que você usou para desenvolver a atividade.")
        print("Digite 'FIM' em uma linha separada para finalizar.")
        codigo = []
        while True:
            linha = input()
            if linha.strip() == "FIM":
                break
            codigo.append(linha)
        codigo_entregue = "\n".join(codigo)
        # Aqui você pode salvar em arquivo, enviar para avaliação, etc.
        print("\nCódigo recebido com sucesso! Obrigado por participar.")
    else:
        print("Tudo bem! Você pode entregar a atividade quando estiver pronto.")
    