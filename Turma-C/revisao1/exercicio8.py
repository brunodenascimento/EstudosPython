#código que receba o valor da base e altura  e calcule a área do triângulo e receba um lado depois e calcula área do quadrado
#fórmula A=(base x altura) / 2
#formula quadrado a=base x altura
opcao=0
while opcao!=3:
    opcao = int(input("Escolha uma opção:\n1 - cálculo da área do triângulo\n2 - cálculo da área do quadrado\n3 - para sair "))
    if opcao==1:
        base=float(input("Digite a base: "))
        altura=float(input("Digite a altura: "))
        a=(base*altura)/2
        print(f"A área do triângulo é {a}.")
    elif opcao==2:
        lado=float(input("Digite o lado do quadrado: "))
        aq=lado**2
        print(f"A área do quadrado é {aq}")
    elif opcao==3:
        print("FIM DO PROGRAMA")
    else:
        print("opção inválida")