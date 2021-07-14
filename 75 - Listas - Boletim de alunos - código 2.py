    # - DESCREVENDO O DESAFIO
print('75 - Crie um programa que leia nome e duas notas de vários alunos',end='')
print('e guarde tudo em uma lista composta. No final, mostre um boletim contendo',end='')
print('a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente')
print()

    #INICIALIZANDO O PROGRAMA
    

        # IMPORTA BIBLIOTECAS



            # 1 - RECEBE DADOS

alunos=list()

while True:
        nome=str(input('nome: '))
        n1=float(input('nota 1: '))
        n2=float(input('nota 2: '))
        media=(n1+n2)/2
        alunos.append([nome,[n1,n2],media])
        deseja_continuar = str(input('continuar?: ')).strip().upper()[0]

    
            # 2 - MANIPULA DADOS, RETORNA DADOS

        if deseja_continuar in 'N':
            break

print(f'{"N":<4}{"NOME":<10}{"MEDIA":>8}')

for index,conteudo in enumerate(alunos):
        print(f'{index:<4}{conteudo[0]:<10}{conteudo[2]:>8}')

while True:
        ver_esse_aluno = int(input('gostaria de mostrar as notas de qual aluno? [999 para parar]: '))
        if ver_esse_aluno == 999:
            print("PROGRAMA ENCERRADO")
            break
        if ver_esse_aluno <= len(alunos)-1:
            print(f'Notas do {alunos[ver_esse_aluno][0]}: {alunos[ver_esse_aluno][1]}')

    






