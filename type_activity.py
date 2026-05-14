def type_activity():
    """Função para validar o tipo de atividade avaliativa
    """
    permitido = [
        "Atividade Avaliativa Individual",
        "Avaliação Continuada",
        "Avaliação Semestral",
    ]
    permitido_lower = [a.lower() for a in permitido]

    tipo_atividade = input("Por favor, informe o tipo de atividade avaliativa (ex: Atividade Avaliativa Individual, Avaliação Continuada, Avaliação Semestral): ").strip()
    while tipo_atividade.lower() not in permitido_lower:
        print("Tipo de atividade inválido. Por favor, tente novamente.")
        tipo_atividade = input("Por favor, informe o tipo de atividade avaliativa (ex: Atividade Avaliativa Individual, Avaliação Continuada, Avaliação Semestral): ").strip()

    # Retorna a forma canônica (mesma capitalização/acentuação definida em `allowed`)
    idx = permitido_lower.index(tipo_atividade.lower())
    return permitido[idx]

    