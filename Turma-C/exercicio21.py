#ler 10 notas de alunos e
numerosvalidos=0
soma=0
media=0
for contador in range (1, 11, 1):
    notas=float(input("Digite a nota: "))
    if notas<=10 and notas>=0:
        soma=soma+notas
        numerosvalidos=numerosvalidos+1

if numerosvalidos==0 or soma<=0:
    print("Você não digitou nenhuma nota válida. Tente novamente!!!")
else:
    media=soma/numerosvalidos
    print(f"{media} {numerosvalidos}")



