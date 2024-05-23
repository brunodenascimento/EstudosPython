from ClasseTicket import *

t1 = Ticket(20)
t2 = Ticketvip(t1.valor)#t2 recebe como parâmetro o valor do atributo "valor" da instância t1classe Ticket
t1.imprimevalor()
retorno=t2.imprimevalor()
print(retorno)

