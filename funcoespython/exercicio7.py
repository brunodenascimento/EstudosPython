from funcoes import exercicio7
nome=input("Digite o nome do produto: ")
quantidade=int(input("Digite a quantidade em estoque: "))
valor=float(input("Agora digite o valor unitário: "))

resposta = exercicio7(nome, quantidade, valor) #resposta recebe o retorno da função exercicio7
print(resposta)