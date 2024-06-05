#refazer exercicio anterior com estrutura de repetição

nota=0
soma=0
for contador in range (0, 2, 1):
    nota=(float(input("Digite a "+str(contador+1)+"º nota: ")))
    while nota>10 or nota<0:
        nota=(float(input("Digite a "+str(contador+1)+"º nota novamente (entre 0 e 10):  ")))
    soma=soma+nota
media=soma/2
print("A média aritmética é: ", media)