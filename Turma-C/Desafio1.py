h1=int(input("Digite o primeiro horário: "))
min1=int(input("Digite o primeiro minuto: "))
print(f"{h1}:`{min1}")
h2=int(input("Digite o segundo horário: "))
min2=int(input("Digite o segundo minuto: "))
print(f"{h2}:{min2}")

if h1>12:
    h1=h1-12
if h2>12:
    h2=h2-12
hora=h1+h2
if hora>12:
    hora=hora-12

minutos = min1+min2
if minutos>=60:
    minutos=minutos-60
    hora=hora+1
print(f"{hora}:{minutos}")

