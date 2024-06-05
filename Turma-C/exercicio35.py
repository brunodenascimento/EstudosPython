#preencher um vetor A com 10 numeros logo em seguida ler mais um numero e guardar em outra variavel B simples
#armmazenar num vetor C o resultado de cada elemento de A multiplicado pelo valor de B
#no final imprimir o vetor C

a=[0,0,0,0,0,0,0,0,0,0]
c=[0,0,0,0,0,0,0,0,0,0]
for contador1 in range (0, len(a), 1):
    a[contador1]=int(input("Digite o valor "+ str(contador1+1)+ ": "))
b=int(input("Por qual número você quer multiplicar esses 10 valores? "))
for contador2 in range (0, len(a), 1):
    c[contador2]=a[contador2]*b
    print(a[contador2], end=" ")
print("\nMultiplicado por ", b, " é igual a:", end="\n")
for contador3 in range (0, len(c), 1):
    print(c[contador3], end=" ")



