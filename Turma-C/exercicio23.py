contador=1
soma=0
numeroalunos=int(input("Digite o número de alunos: "))
while contador<numeroalunos+1:
    notas=float(input("Digite a nota dos alunos em ordem: "))
    soma=soma+notas
    contador=contador+1
media=soma/numeroalunos

print(f"A média da turma é: {media}")

