class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de {valor} realizado. Saldo atual: {self.saldo}")
        else:
            print("O valor do depósito deve ser maior que zero.")
    
    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de {valor} realizado. Saldo atual: {self.saldo}")
        else:
            print("Valor de saque inválido ou saldo insuficiente.")

titular_da_conta = "João"
conta = ContaBancaria(titular_da_conta, 1000)
conta.depositar(500)
conta.sacar(200)