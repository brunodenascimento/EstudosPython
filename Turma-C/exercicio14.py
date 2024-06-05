#mostrar tabuada do numero que o  usuario digitar
n=int(input("Digite o número que você quer saber a tabuada: "))
tabuada=0

if n>10 or n<0:
    print("A tabuada escolhida só pode ser de 1 a 10 ")
else:
    for contador in range(0, 11, 1):
        tabuada=n*contador
        print(f"{n}x{contador}={tabuada}")
