#ler 10 valores e escrever a média aritmetica desses valores
soma=0
media=0
for contador in range (1, 11, 1):
    valor=float(input("Digite um valor: "))
    soma=soma+valor
media=soma/10
print(f"A média aritmética dos 10 valores equivale a: {media}")
