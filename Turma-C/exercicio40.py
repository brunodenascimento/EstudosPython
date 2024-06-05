#faça um programa para let um vetor de 10 números e após isso pedir mais um numero A
#calcular e escrever quantas vezes A foi digitado entre os 10
numeros=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
soma=0
for contador in range (0, 10, 1):
    numeros[contador]=int(input("Digite o número "+str(contador+1)+": "))
vezes=int(input("Digite um número qualquer que será calculado quantas vezes ele foi digitado entre esses 10 anteriores: "))
for contador1 in range (0, 10, 1):
    if numeros[contador1]==vezes:
        soma=soma+1
print(f"O número {vezes} foi digitado {soma} vezes por você.")