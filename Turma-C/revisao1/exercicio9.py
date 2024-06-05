#receba 4 numeros e realize a soma deles a mostre depois a média entre eles

soma=0
for contador in range (0, 4, 1):
    numeros=int(input("Digite o "+str(contador+1)+"º número: "))
    soma=soma+numeros
media=soma/4
print(f"A média desses números é: {media} e a soma desses números é {soma}")