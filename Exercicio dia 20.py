alunos = []


while True:
    aluno = {}
    aluno ['Nome'] = input('Digite seu nome: ')
    aluno ['Media'] = float(input('Digite sua media: '))
    alunos.append(aluno)
    for v in aluno.values():
        if type(v) == float:
            if v >= 7:
                print(f'Aluno {aluno["Nome"]} Aprovado com a média { aluno["Media"]}')
            elif 4 <= v < 7 :
                print(f'Aluno {aluno["Nome"]} em recuperão com a média { aluno["Media"]}')
            else:
                print(f'Aluno {aluno["Nome"]} Reprovado com a média { aluno["Media"]}')
    escolha = input('Deseja continuar ? [S/N] ').upper()
    if escolha == 'N':
        break
print('Lista final dos alunos')
for a in alunos:
    print(f"Nome: {a['Nome']}, Média:{a ['Media']}")
     
    
