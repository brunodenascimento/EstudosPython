time1 = input(print("Digite o nome do primeiro time: "))
golstime1 = int(input(print("Agora infome quantos gols o time: ", time1, " fez")))

time2 = input(print("Digite o nome do segundo time: "))
golstime2 = int(input(print("Agora infome quantos gols o time: ", time2, " fez")))

if golstime1==golstime2:
    print("EMPATE")
elif golstime1>golstime2:
    print("Time ", time1, " campeão com ", golstime1, " gols.")
else:
    print("Time ", time2, " campeão com ", golstime2, " gols.")

