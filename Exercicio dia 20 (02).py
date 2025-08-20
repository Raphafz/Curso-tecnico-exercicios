from random import randint

jogos = []
cont = 1

for i in range(0,4):
    jogadores = {}
    jogadores['Nome'] = input(f'Digite o nome do jogador {cont}º: ')
    cont += 1
    jogadores['Dados'] = randint (1,6)
    jogos.append(jogadores)

rank = sorted (jogos, key=lambda x: x ['Dados'], reverse=True)
print("\nDados jogados:")
for i, jogo in enumerate(rank, start=1):
    print(f"O Ranking final foi: jogador: {jogo['Nome']}, Dado:{jogo['Dados']}") 