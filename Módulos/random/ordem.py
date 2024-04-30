import random
aluno_1 = input("Informe o nome do aluno 1: ")
aluno_2 = input("Informe o nome do aluno 2: ")
aluno_3 = input("Informe o nome do aluno 3: ")
aluno_4 = input("Informe o nome do aluno 4: ")
alunos = [aluno_1, aluno_2, aluno_3, aluno_4]
random.shuffle(alunos)
print("Ordem de apresentação dos alunos:")
print(alunos)
