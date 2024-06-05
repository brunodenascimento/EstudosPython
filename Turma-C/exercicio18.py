guardanegativos=0
for contador in range (1, 11, 1):
    num=int(input("Digite um valor: "))
    if num<0:
        guardanegativos=guardanegativos+1
print(f"Dos valores digitadors, {guardanegativos} são negativos.")
