def deliver_activity():
    """
    Função para validar a entrega da atividade.
    """
    iniciar_entrega_atividade = input("Professor,você deseja iniciar a entrega das atividade? (sim/não): ")
    while iniciar_entrega_atividade.lower() not in ["sim", "não"]:
        print("Resposta inválida. Por favor, responda com 'sim' ou 'não'.")
        iniciar_entrega_atividade = input("Professor, você deseja iniciar a entrega da atividade? (sim/não): ")
    if iniciar_entrega_atividade.lower() == "sim":
        print("Ótimo! Vamos começar a entrega da atividade.")
    else:
        print("Tudo bem! Você deseja adicionar mais tempo para a entrega da atividade? (sim/não): ")
        adicionar_tempo = input("Professor, você deseja adicionar mais tempo para a entrega da atividade? (sim/não): ")
        while adicionar_tempo.lower() not in ["sim", "não"]:
            print("Resposta inválida. Por favor, responda com 'sim' ou 'não'.")
            adicionar_tempo = input("Professor, você deseja adicionar mais tempo para a entrega da atividade? (sim/não): ")
        if adicionar_tempo.lower() == "sim":
            quantidade_tempo = int(input("Quantos minutos você deseja adicionar para a entrega da atividade? (máximo 30 minutos): "))
            while quantidade_tempo < 1 or quantidade_tempo > 30:
                print("Quantidade de tempo inválida. Por favor, insira um valor entre 1 e 30 minutos.")
                quantidade_tempo = int(input("Quantos minutos você deseja adicionar para a entrega da atividade? (máximo 30 minutos): "))
            print(f"Ótimo! Você adicionou {quantidade_tempo} minutos para a entrega da atividade.")
        else:
            print("Tudo bem! A entrega da atividade permanecerá com o tempo original.")
            
