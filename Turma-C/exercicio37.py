#faça um código que leia 5 nomes de usuários e armazene suas respectivas senhas
#imprimir nome do usuario sua respectiva senha e sua posição no array
usuarios = [""]*5
senha = [0]*5
for contador in range(0, 5, 1):
    usuarios[contador] = input("Digite o nome do usuário "+str(contador+1)+": ")
    senha[contador] = int(input("Digite o a senha do usuário " + str(usuarios[contador])+ ": "))

for contador1 in range(0, 5, 1):
    print(f"usuário {usuarios[contador1]} sua senha é {senha[contador1]} e a sua posição é a {str(contador1+1)}º")