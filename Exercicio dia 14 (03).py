parimpar = [[],[]]

for i in range(1, 8):
    numero = (int(input(f'Digite o {i}º valor: ')))
    if numero % 2 == 0:
        parimpar[0].append(numero)
    else:
        parimpar[1].append(numero)
parimpar[0].sort()
parimpar[1].sort()
print(f'Valores pares: {parimpar[0]}')
print(f'Valores impar: {parimpar[1]}') 