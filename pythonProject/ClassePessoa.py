class Pessoa:
    def __init__(self, nome, peso, idade):#__init__ é o nome dado ao método construtor da classe em python
#o self equivale ao this do java
        self.nome=nome
        self.peso=peso
        self.idade=idade
    def comer (self, alimento="", bebida=""):
        if alimento=="" and bebida=="":
            print(f"{self.nome} não está comendo nem bebendo nada")
        elif alimento=="" and bebida!="":
            print(f"{self.nome}  não está comendo mas está bebendo "+bebida)
        elif alimento != "" and bebida == "":
            print(f"{self.nome} está comendo {alimento} mas não está bebendo")
        else:
            print(f"{self.nome} está comendo {alimento} e está bebendo {bebida}")

    def falar(self, frase=""):#quando eu atribuo um valor vazio a um parametro serve como um valor padrão, ou seja, se nada for passado como parâmetro, vai ser considerado esse valor
        if frase=="":
            print(f"{self.nome} não está falando")
        else:
            print(f"{self.nome} disse: {frase}")

    def dormir(self):
        print(f"{self.nome} está dormindo")






