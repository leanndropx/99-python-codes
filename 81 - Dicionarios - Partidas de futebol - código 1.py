    # - DESCREVENDO O DESAFIO
print('81 - Crie um programa que gerencie o aproveitamento de um jogador de futebol. ',end='')
print('O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade ',end='')
print('de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário ',end='')
print('incluindo o total de gols feitos durante o campeonato. ')
print()

    #INICIALIZANDO O PROGRAMA
    

        # IMPORTA BIBLIOTECAS

from random import randint

            # 1 - RECEBE DADOS

jogo={}
gols=[]
soma_gols=0

jogo['nome']=str(input('nome: '))
jogo['partidas']=int(input('quantas partidas jogou?: '))

for partida in range(0,jogo['partidas']):
        #gol=randint(0,10)
        total_gols = int(input(f'quantos gols ele fez na partida {partida+1}: '))

                # 2 - MANIPULA DADOS

        gols.append(total_gols)
        soma_gols=soma_gols+total_gols

jogo['gols']=gols
jogo['Total de gols']=soma_gols


            # 3 - RETORNA DAODS

print('-__-'*30)
for k,v in jogo.items():
        print(f'{k} tem valor {v}')

print('-__-'*30)
print(f'O jogador {jogo["nome"]} jogou {jogo["partidas"]} partidas')

for index,valor in enumerate(gols):
        print(f'Na partida {index+1} ele fez {valor} gols')









