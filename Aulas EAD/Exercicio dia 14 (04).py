from random import randint


quantidade = int(input("Quantos jogos você quer gerar? "))


jogos = []

for i in range(quantidade):
    jogo = []
    while len(jogo) < 6:
        numero = randint(1, 60)
        if numero not in jogo:
            jogo.append(numero)
    jogo.sort()  
    jogos.append(jogo)


print("\nPalpites da Mega Sena:")
for i, jogo in enumerate(jogos, start=1):
    print(f"Jogo {i}: {jogo}")