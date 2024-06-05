#fazer um código que peça 3 numeros ao usuario e mostrar qual é o maior
#obs: só pode criar uma variavel
maiornumero=0
for contador in range (0, 3, 1):
    numero=int(input("Digite o " + str(contador+1) + "º número: "))
    if numero>maiornumero:
        maiornumero=numero

print("o maior número é: ", maiornumero)
