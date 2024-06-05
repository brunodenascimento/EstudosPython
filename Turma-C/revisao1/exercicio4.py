novamente="sim"
while novamente=="sim":
    idade=int(input("Digite a sua idade: "))
    aniversario=input("Você já fez aniversario? (s//n)")
    anonascimento=2024-idade

    if aniversario=="s" or aniversario=="S":
        print("Você nasceu em ", str(anonascimento))
    else:
        print("Você nasceu em ", str(anonascimento-1))
    novamente=input("Deseja fazer novamente? (sim/qualquer tecla=não)")
else:
    print("FIM DO PROGRAMA")

