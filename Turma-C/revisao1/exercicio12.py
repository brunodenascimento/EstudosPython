inicioxadrez=int(input("Digite que horas o jogo de xadrex começou - apenas horas: "))
fimxadrez=int(input("Digite que horas o jogo de xadrex terminou - apenas horas: "))
if inicioxadrez<fimxadrez:
    duracao=fimxadrez-inicioxadrez
elif inicioxadrez>fimxadrez:
    duracao=(24-inicioxadrez)+fimxadrez
elif inicioxadrez==fimxadrez:
    duracao=24
print(f"O jogo durou {duracao} horas")
