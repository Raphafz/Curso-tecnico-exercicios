nome = []
dado = []
maior = 0
menor = 0
while True:
        dado.append(input('Digite o nome (ou "sair" para encerrar ): '))
        if dado[0] == 'sair'.lower():
                break

        dado.append (float(input(f'Digite seu peso: ')))
        
        if len(nome) == 0:
               maior = menor = dado[1]
        else:
            if dado[1] > maior:
                    maior = dado[1]
            if dado[1] < menor: 
                      menor = dado[1]
        nome.append(dado[:])
        dado.clear()

print(f'Ao todo foram cadastrados {len(nome)}')
print(f'O Maior peso cadastrado foi de {maior} kg. Peso de: ', end="")
for p in nome:
    if p[1] == maior:
           print(f' [{p[0]}]', end='')
print()
print(f' O menor Peso cadastrado foi de {menor}KG. Peso de: ', end="")
for p in nome:
    if p[1] == menor:
           print(f' [{p[0]}]', end='')

