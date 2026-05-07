def teacher_questions ():
    """
    Função para validar dados dos professores. 
    """
    nome_completo_professor = input("Professor por favor digite seu nome completo: ")
    while len(nome_completo_professor) < 5:
        print("O nome completo deve conter pelo menos 5 caracteres. Por favor, tente novamente.")
        nome_completo_professor = input("Professor por favor digite seu nome completo: ")

    email_academico_professor = input("Professor por favor digite seu email acadêmico: ")
    while not email_academico_professor.endswith("@unifecaf.com.br"):
        print("O email deve ser do domínio '@unifecaf.com.br'. Por favor, tente novamente.")
        email_academico_professor = input("Professor por favor digite seu email acadêmico: ")

    disciplina = input("Professor por favor informe a sua disciplina: ")
    while len(disciplina) < 3:
        print("A disciplina deve conter pelo menos 3 caracteres. Por favor, tente novamente.")
        disciplina = input("Professor por favor informe a sua disciplina: ")

    matricula = input("Professor por favor digite sua matrícula: ")
    while not matricula.isdigit() or len(matricula) != 6:
        print("A matrícula deve conter exatamente 6 dígitos numéricos. Por favor, tente novamente.")
        matricula = input("Professor por favor digite sua matrícula: ")