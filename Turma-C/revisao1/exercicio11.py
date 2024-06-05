#faça um programa que leia a idade de uma pessoa expressa em anos, meses e dias e escreva a  idade dessa pessoa expressa apenas
#em dias. Considerar anos com com 365 dias e meses com 30 dias.
print("Digite a sua idade em:")
anos=int(input("Anos - "))
meses=int(input("Meses - "))
dias=int(input("Dias - "))
print((anos*365)+(meses*30)+dias)