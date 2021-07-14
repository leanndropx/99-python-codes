    # - DESCREVENDO O DESAFIO
print('82 - Crie um programa que gerencie o aproveitamento de um jogador de futebol. ',end='')
print('O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade ',end='')
print('de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário ',end='')
print('incluindo o total de gols feitos durante o campeonato. ')
print()

    #INICIALIZANDO O PROGRAMA
    

        # IMPORTA BIBLIOTECAS

from random import randint

            # 1 - RECEBE DADOS

jogador={}
tot=[]

jogador['nome']=str(input('nome: '))
jogador['partidas']=int(input(f'quantas partidas o {jogador["nome"]} jogou?: '))

    
            # 2 - MANIPULA DADOS, CRIA NOVOS DADOS

for c in range(0,jogador['partidas']):
    tot.append(randint(0,10))
jogador['gols']=tot
jogador['total']=sum(jogador['gols'])

            
            # 3 - RETORNA DAODS

print('O total de gols foi {}{}{}'.format('\033[35m',jogador['total'],'\033[m'))
for pos,c in enumerate(jogador['gols']):
    print(f'Na partida {pos+1} o {jogador["nome"]} fez {c} gols')

print()
print(jogador)







