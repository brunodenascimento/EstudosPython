class Contabancaria:
    def __init__(self, numeroConta, tipoConta):
        self.numeroConta=numeroConta
        self.saldoConta=0
        self.tipoConta=tipoConta
        self.statusConta=False
        #métodos - depositar, sacar, verificar saldo e poder ativar e desativar conta
    def depositar (self, valor):
        if self.statusConta==False:
            print("Sua conta está desativada. Ative ela para receber depósitos")
        elif valor<=0:
            print("Não é possível depositar um valor equivalente ou inferior a 0")
        else:
            self.saldoConta=self.saldoConta+valor
            print(f"Você depositou R${valor}. Saldo atual = {self.saldoConta}")

    def sacar (self, valor):
        if self.statusConta==False:
            print("Sua conta está desativada. Ative ela para realizar saques")
        elif self.saldoConta<valor:
            print("Sem saldo o suficiente para efetuar o saque")
        else:
            self.saldoConta=self.saldoConta-valor
            print(f"Você sacou R${valor}. Saldo atual = {self.saldoConta}")

    def ativarConta(self):
        if self.statusConta==True:
            print("Sua conta já está ativa.")
        else:
            self.statusConta=True
            print("Conta ativada com sucesso.")

    def desativarConta(self):
        if self.saldoConta>0:
            print(f"Sua conta ainda tem R${self.saldoConta} reais. Zere todo o saldo para que seja possível desativar.")
        elif self.statusConta==False:
            print("Sua conta já está desativada.")
        else:
            self.statusConta=False
            print("Conta desativada com sucesso.")

    def vefificarSaldo(self):
        if self.statusConta==False:
            print("Sua conta está desativada. Ative ela para poder realizar verificações")
        else:
            print(f"Saldo atual da sua conta: R${self.saldoConta}.")


