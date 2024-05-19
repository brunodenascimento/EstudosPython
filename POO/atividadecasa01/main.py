from ClassePessoa import *

p1 = ClassePessoa("Céu", 20, 80)
p2 = ClassePessoa ("Céu", 20, 80)

print(p1.nome) #printar um atributo da instanciação p1
p2.dormir()
p2.comer("guarana")
p2.parardecomer()
p2.dormir()
p2.parardedormir()
p2.falar("OIII")