n=int(input("Digite um número maior do que zero: "))
if n<=0:
    print("Digite um número válido")
else:
    for contador in range(1, n+1, 1):
        print(contador)