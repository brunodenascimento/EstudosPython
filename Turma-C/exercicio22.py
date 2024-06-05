#laço de repetição while
x=0
soma=0
media=0
while x<10:
    valor=float(input("Digite um número: "))
    soma=soma+valor
    x=x+1
media=soma/10

print(f"{media}")