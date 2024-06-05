n1=float(input("Digite o número: "))
n2=int(input("Agora digite o segundo número: "))
while n2==0:
    n2=int(input("Digite um número válido, pois o número 0 não é aceito: "))
divisao=n1/n2
print(f"Resultado da divisão: {divisao}")