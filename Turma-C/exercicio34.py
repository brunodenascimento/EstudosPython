#escreva um código que permita a leitura das notas de uma turma de 5 alunos e guarde num vetor.
#Calcular a média da turma e contar quantos alunos obtiveram a nota máxima dessa média calculada.
#Escrever a média da turma e o resultado da contagem

notasAlunos=[0, 0, 0, 0, 0,]
quantidadeaprovados=0
mediaturma=0
notatotal=0
for contador0 in range (0, len(notasAlunos), 1):
    notasAlunos[contador0]=float(input("Digite a nota do aluno: "))
for contador1 in range (0, len(notasAlunos), 1):
    print("nota do aluno ", contador1+1, " é ", notasAlunos[contador1], end="\n")
    notatotal = notatotal + notasAlunos[contador1]
mediaturma = notatotal / len(notasAlunos)
print(f"Média da turma: {mediaturma}")
for contador2 in range (0, len(notasAlunos), 1):
    if notasAlunos[contador2]>=mediaturma:
        quantidadeaprovados=quantidadeaprovados+1
print(quantidadeaprovados, "foram aprovados")


