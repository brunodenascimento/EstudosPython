#criar duas variáveis A e B que possuem valores distintos a=5 e b=10. Faça um algoritmo que guarde esses dois valores nessas duas variáveis  em seguida, mostre os valores trocados.

a=input(print("Digite o primeiro valor \n"))
b=input(print("Digite o segundo valor \n"))
print( "Você digitou:", a, b,"\n")
c=a
a=b
b=c
print("Valores invertidos:", a, b)
