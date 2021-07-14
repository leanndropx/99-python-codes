    # - DESCREVENDO O DESAFIO
print('74 - Crie um programa que leia nome e duas notas de vários alunos',end='')
print('e guarde tudo em uma lista composta. No final, mostre um boletim contendo',end='')
print('a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente')
print()

    #INICIALIZANDO O PROGRAMA
    

        # IMPORTA BIBLIOTECAS



            # 1 - RECEBE DADOS

um_aluno = list()
alunos = list()

while True:
        um_aluno.append(str(input('Nome: ')))
        um_aluno.append(float(input('Nota 1: ')))
        um_aluno.append(float(input('Nota 2: ')))
        um_aluno.append((um_aluno[1]+um_aluno[2])/2)
        
        alunos.append(um_aluno[:])
        um_aluno.clear()
        
        deseja_continuar = str(input('gostaria de continuar?: ')).strip().upper()[0]
        
        while deseja_continuar not in 'SN':
            deseja_continuar = str(input('ERRO. Digite novamente [S/N]: ')).strip().upper()[0]
        
        if deseja_continuar == 'N':
            break


    
            # 2 - MANIPULA DADOS, RETORNA DADOS CONFORME CONDICAO

print(f'{"  "}{"NOME":^21}{"MEDIA":^7}{"NOTA 1":^10}{"NOTA 2":^10}')


for aluno in range(0,len(alunos)):

        print(f'{"  "}{aluno+1}{alunos[aluno][0].upper():^21}',end='')
        
        print('{:^6.2f}'.format(alunos[aluno][3]),end='')
        
        print(f'{alunos[aluno][1]:^10}',end='')
        
        print(f'{alunos[aluno][2]:^10}')

while True:
        ver_esse_aluno = int(input('gostaria de ver a nota de qual aluno?: '))

        if ver_esse_aluno == 999:
            break
        print(f'nota { alunos [ver_esse_aluno - 1] [0] }:')
        
        print(f'nota 1: { alunos [ver_esse_aluno - 1] [1] }')
        
        print(f'nota 2: {alunos [ver_esse_aluno - 1] [2] }')


print(' ')
print(alunos)


            






