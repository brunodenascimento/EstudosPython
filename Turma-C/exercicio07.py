nota1=float(input("Digite a primeira nota do aluno: "))
nota2=float(input("\nDigite a segunda nota do aluno: "))
nota3=float(input("\nDigite a terceira nota do aluno: "))
media=((nota1+nota2+nota3)/3)
print("sua média final foi: ", media, "\n")
if media>=7:
    print("Aprovado")
elif media>=4:
    print("Recuperação")
else:
    print("Reprovado")