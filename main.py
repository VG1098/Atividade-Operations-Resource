from teacher_questions import teacher_questions
from type_activity import type_activity
from activity_score import pontuacao_maxima_atividade
from student_group import student_group
from student_questions import student_questions
from date_activity import date_questions
from activity_duration import activity_duration
from start_activity import start_activity
from deliver_activity import deliver_activity
from git_hub_question import git_hub_question

def main():
	print("Seja bem vindo, esta é uma atividade de Python da disciplina Operations Resource")

	print("A seguir, serão feitas algumas validações de dados, para isso, por favor, insira os seguintes dados:")

	teacher_questions()
	type_activity()
	pontuacao_maxima_atividade()
	is_grupo, quantidade_integrantes = student_group()
	student_questions(is_grupo, quantidade_integrantes)
	date_questions()
	activity_duration()
	start_activity()
	deliver_activity()
	git_hub_question()
	

 
if __name__ == "__main__":
	main()
