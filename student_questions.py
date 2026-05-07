def student_questions(is_grupo=False, quantidade_integrantes=1):
    """
    Função para validar os dados de um aluno ou de todos os integrantes de um grupo.
    """
    def validar_dados_aluno(rotulo_aluno):
        nome_completo = input(f"Digite o nome completo do {rotulo_aluno}: ")
        while len(nome_completo.strip()) < 5:
            print("O nome completo deve conter pelo menos 5 caracteres. Por favor, tente novamente.")
            nome_completo = input(f"Digite o nome completo do {rotulo_aluno}: ")

        email_academico = input(f"Digite o email acadêmico do {rotulo_aluno}: ")
        while not email_academico.lower().endswith("@unifecaf.com.br"):
            print("O email deve ser do domínio '@unifecaf.com.br'. Por favor, tente novamente.")
            email_academico = input(f"Digite o email acadêmico do {rotulo_aluno}: ")

        ra = input(f"Digite o RA do {rotulo_aluno}: ")
        while not ra.isdigit() or len(ra) != 6:
            print("O RA deve conter exatamente 6 dígitos numéricos. Por favor, tente novamente.")
            ra = input(f"Digite o RA do {rotulo_aluno}: ")

    total_alunos = quantidade_integrantes if is_grupo else 1
    for indice in range(1, total_alunos + 1):
        if is_grupo:
            print(f"\nValidando o integrante {indice} de {total_alunos}.")
            rotulo_aluno = f"integrante {indice}"
        else:
            print("\nValidando o aluno.")
            rotulo_aluno = "aluno"
        validar_dados_aluno(rotulo_aluno)

    if is_grupo:
        print("Todos os integrantes do grupo foram validados com sucesso.")
    else:
        print("Dados do aluno validados com sucesso.")


