#algoritmo que vai ler 10 numeros e ao  final imprimir a soma dos 10 numero
soma=0
for contador in range(1, 11, 1):
    valor=int(input("Digite o valor: "))
    soma=soma+valor

print(soma)