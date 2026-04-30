def questions():
    """
    Função para realizar perguntas ao usuário e validar as respostas.
    """
    nome_completo = input("Digite seu nome completo: ")
    while len(nome_completo) < 5:
        print("O nome completo deve conter pelo menos 5 caracteres. Por favor, tente novamente.")
        nome_completo = input("Digite seu nome completo: ")

    email_academico = input("Digite seu email acadêmico: ")
    while not email_academico.endswith("@unifecaf.com.br"):
        print("O email deve ser do domínio '@unifecaf.com.br'. Por favor, tente novamente.")
        email_academico = input("Digite seu email acadêmico: ")
    
    ra = input("Digite seu RA: ")
    while not ra.isdigit() or len(ra) != 6:
        print("O RA deve conter exatamente 6 dígitos numéricos. Por favor, tente novamente.")
        ra = input("Digite seu RA: ")
    
    
