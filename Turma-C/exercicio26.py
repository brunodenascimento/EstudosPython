#fazer um código que peça uma 1ª e uma 2ª nota de um aluno e caso uma das nota2 não estejam entre 0 e 10, fique pedindo novamente
refazer="S"
while refazer=="S" or refazer=="s":
    nota1 = float(input("Digite a primeira nota: "))
    while nota1 <0 or nota1 >10:
            nota1=float(input("Digite  um número válido para a primeira nota: "))

    nota2 = float(input("Digite a segunda nota: "))
    while nota2 < 0 or nota2 > 10:
        nota2=float(input("Digite  um número válido para a segunda nota: "))
    media=(nota1+nota2)/2
    print(f"A média da nota desse aluno é: {media}")
    refazer=input("Desejo realizar cálculo novamente? (S=sim/N=não) ")
if refazer=="n" or refazer=="N:":
    print("Obrigado por participar.")






