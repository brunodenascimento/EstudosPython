class ClassePessoa:
    def __init__(self, nome, peso, idade):#__init__ é o nome dado ao método construtor da classe em python
#o self equivale ao this do java
        self.nome=nome
        self.peso=peso
        self.idade=idade
        self.comendo=False
        self.dormindo=False
        self.falando=False
    def comer (self, alimento="", bebida=""):
        if self.dormindo==True or self.falando==True:
            print("Eu não posso comer enquanto estou dormindo ou falando")
        elif alimento=="" and bebida=="":
            print(f"{self.nome} não está comendo nem bebendo nada")
        elif alimento=="" and bebida!="":
            print(f"{self.nome}  não está comendo mas está bebendo "+bebida)
            self.comendo = True
        elif alimento != "" and bebida == "":
            print(f"{self.nome} está comendo {alimento} mas não está bebendo")
            self.comendo = True
        else:
            print(f"{self.nome} está comendo {alimento} e está bebendo {bebida}")
            self.comendo = True

    def falar(self, frase=""):#quando eu atribuo um valor vazio a um parametro serve como um valor padrão, ou seja, se nada for passado como parâmetro, vai ser considerado esse valor
        if self.comendo==True or self.dormindo==True:
            print("Eu não posso falar enquanto estou comendo ou dormindo")
        elif frase=="":
            print(f"{self.nome} não está falando")
        else:
            print(f"{self.nome} disse: {frase}")
            self.falando=True

    def dormir(self):
        if self.comendo==True or self.falando==True:
            print("Eu não posso dormir enquanto estou comendo ou falando")
        else:
            print(f"{self.nome} está dormindo")
            self.dormindo=True

    def parardedormir(self):
        if self.dormindo==False:
            print("Eu já não estou dormindo.")
        else:
            self.dormindo=False

    def parardecomer(self):
        if self.comendo == False:
            print("Eu já não estou comendo.")
        else:
            self.comendo=False

    def parardefalar(self):
        if self.falando == False:
            print("Eu já não estou falando.")
        else:
            self.falando=False