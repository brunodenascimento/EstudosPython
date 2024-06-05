#fazer um código que peça uma 1ª e uma 2ª nota de um aluno e caso uma das nota2 não estejam entre 0 e 10, fique pedindo novamente
#com base no exercicio anterior, mostrar a média da turma no final
mediaturma=0
mediaturma=0
alunos=int(input("Digite a quantidade de alunos que você irá verificar a nota: "))
for alunos in range (0, alunos, 1):
    nota1 = float(input("Digite a primeira nota: "))
    while nota1 <0 or nota1 >10:
            nota1=float(input("Digite  um número válido para a primeira nota: "))

    nota2 = float(input("Digite a segunda nota: "))
    while nota2 < 0 or nota2 > 10:
        nota2=float(input("Digite  um número válido para a segunda nota: "))
    media=(nota1+nota2)/2
    print(f"A média da nota desse aluno é: {media}")
    mediaturma=mediaturma+media
media=mediaturma/2
print(f"Média total da sala {media}")







