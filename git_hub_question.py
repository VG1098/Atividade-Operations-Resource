def git_hub_question():
    """
    Função para envio do link do repositório do GitHub para a atividade de Python da disciplina Operations Resource.
    """
    pergunta1 = input("Você deseja acessar o repositório do GitHub para esta atividade? (sim/não): ").strip().lower()
    if pergunta1 == "sim":
        print("Ótimo! Você pode acessar o repositório do GitHub através do seguinte link: https://github.com/gustavobrazdev/aula-faculdade")
    elif pergunta1 == "não":
        print("Ok, sem problemas!")
    else:
        print("Resposta inválida. Por favor, responda com 'sim' ou 'não'.")
        git_hub_question()