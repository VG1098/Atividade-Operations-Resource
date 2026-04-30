from personal_questions import questions
from date_activity import date_questions
from start_activity import start_activity
from deliver_activity import deliver_activity

def main():
	print("Seja bem vindo, esta é uma atividade de Python da disciplina Operations Resource")

	print("A seguir, serão feitas algumas validações de dados, para isso, por favor, insira os seguintes dados:")
	questions()
	date_questions()
	start_activity()
	deliver_activity()
	


if __name__ == "__main__":
	main()
