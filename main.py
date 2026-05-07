from teacher_questions import teacher_questions
from student_group import student_group
from student_questions import student_questions
from date_activity import date_questions
from start_activity import start_activity
from git_hub_question import git_hub_question

def main():
	print("Seja bem vindo, esta é uma atividade de Python da disciplina Operations Resource")

	print("A seguir, serão feitas algumas validações de dados, para isso, por favor, insira os seguintes dados:")

	teacher_questions()
	is_grupo, quantidade_integrantes = student_group()
	student_questions(is_grupo, quantidade_integrantes)
	date_questions()
	start_activity()
	git_hub_question()
	


if __name__ == "__main__":
	main()
