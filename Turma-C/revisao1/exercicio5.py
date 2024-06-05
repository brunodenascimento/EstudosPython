
numero=[0, 0, 0]
maior=numero[0]
for contador in range (0, len(numero), 1):
    numero[contador]=int(input("Digite o " + str(contador+1) + "º número: "))
if numero[1]>numero[0] and numero[1]>numero[2]:
    maior=numero[1]
else:
    maior=numero[2]
print(maior)
