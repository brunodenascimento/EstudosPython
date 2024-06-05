#faça um código pra ler 5 numeros e armazenas em um vetor. após a leitura o código deve escrever em ordem inversa
a=[0,0,0,0,0]
for contador1 in range (0, len(a), 1):
    a[contador1]=int(input("Digite o valor "+ str(contador1+1)+ ": "))
for contador2 in range (len(a)-1, -1, -1): #preciso colocar -1 no len pois o vetor só vai até a posição 4 (0,1,2,3,4)
#ele vai até -1, pois precisa contar 5 vezes
    print(a[contador2], end=" ")
