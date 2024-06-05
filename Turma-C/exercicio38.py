#faça um código que leia 5 nomes de usuários e armazene suas respectivas senhas
#depois fazer um sistema de login que se forem coincidentes mostre "login efetuado com sucesso"
opcao=0
une=0
while opcao!=3:
    opcao=int(input("Escolha:\n1 - Para fazer o cadastro\n2 - Para fazer o login\n3 - Para sair: "))
    if opcao==1:
        usuarios = ["", "", "", "", ""]
        senhas = [0, 0, 0, 0, 0]
        for contador in range(0, 5, 1):
            usuarios[contador] = input("Digite o nome do usuário " + str(contador + 1) + ": ")
            senhas[contador] = int(input("Digite o a senha do usuário " + str(usuarios[contador]) + ": "))

        for contador1 in range(0, 5, 1):
            print(f"usuário {usuarios[contador1]} sua senha é {senhas[contador1]} e a sua posição é a {str(contador1 + 1)}º")
    elif opcao==2:
        usuario = input("Digite o nome do usuario: ")
        senha = int(input("Digite a senha do usuario: "))
        for contador2 in range (0, 5, 1):
            if usuario==usuarios[contador2]:
                if senha==senhas[contador2]:
                    print("login efetuado com sucesso!")
                else:
                    print("Senha incorreta.")
            else:
                une=une+1
        if une==5:
            print("Usuário não encontrado")
else:
    print("Fim do programa!")

