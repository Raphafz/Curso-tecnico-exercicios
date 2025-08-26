saldo = 0
class Saldo():
    def __init__(self, valor):
        self.valor = valor
    def depositar(self):
        global saldo
        saldo += self.valor
        print (f'O seu saldo é R$ {self.valor}')

deposito = float(input('Qual o valor do deposito? '))
transacao = Saldo(deposito)
transacao.depositar()

        