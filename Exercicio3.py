num = []
for i in range(0, 5):
    numero = int(input("Digite os numeros: "))
    if i == 0 or numero > num [-1]:
        num.append(numero)
        print('Valor adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(num):
            if numero <= num[pos]:
                num.insert(pos, numero)
                print(f'Valor {num} adicionando na posição {pos} da lista')
                break
            pos += 1
        
print(f' Os valores em ordem são: {num}')
   
