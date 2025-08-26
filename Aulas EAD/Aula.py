numero = []
for i in range(0, 5):
    numero.append(int(input(f'Digite um valor para a posição {i}: ')))
    
num_max = max(numero)
num_min = min(numero)
pos_max = [i for i, num in enumerate(numero) if num == num_max]
pos_min = [i for i, num in enumerate(numero) if num == num_min]
print(f"O maior número da lista é: {num_max} na posição {pos_max}")
print(f"O menor número da lista é: {num_min} na posição {pos_min}")

print("Lista completa:", numero)
