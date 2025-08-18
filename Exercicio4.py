numero = []
par = []
impar = []

while True:
    num = int(input('Digite um valor: '))
    
    if num not in numero:
        numero.append(num)
        print('Valor adicionado na lista!')
        
        if num % 2 == 0:
            par.append(num)
        else:
            impar.append(num)
    else:
        print('Valor já existe na lista!')
    
    resposta = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if resposta == 'N':
        break

print(f'\nOs valores digitados foram: {numero}')
print(f'Os valores pares são: {par}')
print(f'Os valores ímpares são: {impar}')