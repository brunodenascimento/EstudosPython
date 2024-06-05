#leia um numero diferente de 0 e diga se esse numero é positivo ou negativo no final diga se ele quer fazer novamente
novamente="s"

while novamente=="s" or novamente=="S":
    numero=int(input("Digite um número: "))
    while numero==0:
        numero=int(input("Digite um número diferente de 0: "))
    if numero<0:
        print(f"{numero} é um valor negativo.")
    else:
        print(f"{numero} é um valor positivo.")
    novamente=input("Deseja fazer novamente o código?? S=sim // Qualquer tecla=não ")
else:
    print("FIM DO PROGRAMA.")
