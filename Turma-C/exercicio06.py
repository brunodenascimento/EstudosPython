#receba dois numeros do usuario e mostre eles em ordem crescente

n1 = int(input("Digite o primeiro numero: \n"))
n2 = int(input("Digite o segundo numero: \n"))

if n1 == n2:
    print("Os números digitados são iguais")
elif n1 > n2:
    print(n2, n1)
else:
    print(n1, n2)