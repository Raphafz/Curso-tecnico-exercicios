numero = []

while True:
    num = int(input('Digite um valor: '))
    if num not in numero:
        numero.append(num)
        print('Valor adicionado na lista!')
    else:
        print('Valor já existe na lista!')
    
    resposta = str(input('Quer continuar? [S/N]: '))
    if resposta in 'Nn':
        break
print(f'Numeros digitados:{numero}')
numero.sort()
print(f'Numeros digitados em ordem crescente :{numero}')
numero.sort(reverse= True)
print(f'Numeros digitados em ordem decrescente :{numero}')