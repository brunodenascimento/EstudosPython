litro=float(input("Digite quantos litros de combustivel você comprou: "))
combustivel=input("Digite o combustível escolhido: \nG=Gasolina\nE=Etanol\n")
precofinal=0

if combustivel=="G" or combustivel=="g":
    precofinal=litro*5.80
    print("Valor final Gasolina: ", precofinal)
elif combustivel=="E" or combustivel=="e":
    precofinal=litro*4.90
    print("Valor final Etanol: ", precofinal)
else:
    print("Opção Inválida!\nEscolha gasolina ou etanol.")