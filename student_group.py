def student_group():
    """
    Função para identificar se a atividade será feita em grupo e quantos integrantes serão validados.
    """
    pergunta1 = input("A atividade será feita em grupo? (sim/não): ")
    while pergunta1.lower() not in ["sim", "não"]:
        print("Resposta inválida. Por favor, responda com 'sim' ou 'não'.")
        pergunta1 = input("A atividade será feita em grupo? (sim/não): ")
    if pergunta1.lower() == "sim":
        quantidade_integrantes = input("Quantos integrantes tem o grupo? ")
        while not quantidade_integrantes.isdigit() or int(quantidade_integrantes) < 2:
            print("A quantidade de integrantes deve ser um número inteiro maior ou igual a 2. Por favor, tente novamente.")
            quantidade_integrantes = input("Quantos integrantes tem o grupo? ")
        print(f"Ótimo! O grupo tem {quantidade_integrantes} integrantes.")
        return True, int(quantidade_integrantes)
    else:
        print("Tudo bem! Você pode entregar a atividade individualmente.")
        return False, 1