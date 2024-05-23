pontuacao1=0
pontuacao2=0
for contador in range(0, 3, 1):
    print("Round "+str(contador+1))
    jogada1 = int(input("Jogador 1, escolha 1 - Pedra / 2 - Papel / 3 - Tesoura "))
    jogada2 = int(input("Jogador 2, escolha Pedra / 2 - Papel / 3 - Tesoura "))
    if jogada1==jogada2:
        print("Empate")
    elif jogada1==1 and jogada2==2:
        print("Jogador 2 venceu")
        pontuacao2=pontuacao2+1
    elif jogada1==1 and jogada2==3:
        print("Jogador 1 venceu")
        pontuacao1 = pontuacao2 + 1
    elif jogada1==2 and jogada2==1:
        print("Jogador 1 venceu")
        pontuacao1=pontuacao1+1
    elif jogada1==2 and jogada2==3:
        print("Jogador 2 venceu")
        pontuacao2=pontuacao2+1
    elif jogada1==3 and jogada2==1:
        print("Jogador 2 venceu")
        pontuacao2 = pontuacao2 + 1
    elif jogada1==3 and jogada2==2:
        print("Jogador 1 venceu")
        pontuacao1=pontuacao1+1
if pontuacao1>pontuacao2:
    print("Vencedor: jogador 1")
else:
    print("Vencedor: jogador 2")




