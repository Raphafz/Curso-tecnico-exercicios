class Pessoa():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def exibir(self):
        print(f'Olá eu sou o {self.nome} e tenho {self.idade} anos, muito prazer!')

pessoa = (input('Digite seu nome: ')) 
idade = (int(input('Digite sua idade: ')))
apresentacao = Pessoa(pessoa, idade)
apresentacao.exibir()

        