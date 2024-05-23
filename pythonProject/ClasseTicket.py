class Ticket:
    def __init__(self, valor):
        self.valor=valor

    def imprimevalor(self):
        print("Valor do ingresso comum é: "+str(self.valor))

class Ticketvip(Ticket):
    def __init__(self, valor):
        self.valor=valor
        super().__init__(valor)

    def imprimevalor(self):
        self.valorvip=self.valor+self.valor/2
        return "O valor do ingresso vip é "+str(self.valorvip)

