#ler 10  valores e dizer quantos deles estão entre 10 e 20 e quantos deles estão fora do intervalo
intervalodentro=0
intervalofora=0
for contador in range (1, 11, 1):
    numeros=int(input("Digite um valor: "))
    if numeros>=10 and numeros<=20:
        intervalodentro=intervalodentro+1

intervalofora=10-intervalodentro
print(f"Você digitou {intervalodentro} números entre 10 e 20 e {intervalofora} fora desse intervalo.")