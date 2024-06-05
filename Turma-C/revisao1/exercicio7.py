#crie um codigo que peça um numero e diga se ele é par  ou impar e repita o programa até o usuario digitar -99
numero=0
while numero != -99:
    numero=int(input("Digite um número: (caso queira sair do programa digite -99): "))
    if numero%2==0:
        print("O número ", numero, " é par")
    elif numero != -99:
        print("O número ", numero, " é ímpar")
else:
    print("FIM DO PROGRAMA")