# Enunciado: Crie um programa que receba a nota de 5 alunos e exiba quantos foram aprovados (nota maior ou igual a 7
lista_notas = []

for nota in range(5):
    nota = int(float(input("nota do aluno: ")))
    lista_notas.append(nota)
for nota in lista_notas:
    if nota >= 7:
        print ("aprovado")
    else:
        print("reprovado")



