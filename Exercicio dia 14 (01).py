nome = []
dado = []
Maior = 0
Menor = 0
while True:
        dado.append(input('Digite o nome (ou "sair" para encerrar ): '))
        if dado[0] == 'sair':
                break

        dado.append (int(input(f'Digite a idade de: ')))
        nome.append(dado[:])
        dado.clear()
        
        
for dado in nome:
            if dado[1] >= 18:
                print(f'O {dado[0]} é maior de idade!')
                Maior +=1
            else:
                print(f'O {dado[0]} é menor de idade!')
                Menor +=1        
print(f'A quantidade de menor é: {Menor}')
print(f'A quantidade total dos maiores de idade são: {Maior}')