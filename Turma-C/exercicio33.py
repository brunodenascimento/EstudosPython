#criar array tamanho 5 e preencher com nomes de 5 alunos que serão informados pelo usuário
nomes=["", "", "", "", ""]
for contador in range (0, len(nomes), 1):
    nomes[contador]=input("Digite o nome dos 5 alunos: ")
for contador1 in range (0, len(nomes), 1):
    print(f"{contador1} é o nome: {nomes[contador1]}")
