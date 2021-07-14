    # - DESCREVENDO O DESAFIO
print('77 - Crie um programa onde 4 jogadores joguem um dadoe tenham resultados aleatórios.')
print('Guarde esses resultados em um dicionario.')
print('No final, coloque esse dicionario em ordem, sabendo que o vencedor tirou o maior numero no dado')
print()

    #INICIALIZANDO O PROGRAMA
    

        # IMPORTA BIBLIOTECAS

from random import randint
from operator import itemgetter
from time import sleep


            # 1 - RECEBE DADOS

jogo={}
for c in range(0,4):
        jogo[f'jogador {c+1}']=randint(1,6)

    
            # 2 - MANIPULA E CRIA NOVOS DADOS

ranking=[]
ranking=sorted(jogo.items(),key=itemgetter(1),reverse=True)

for k,v in jogo.items():
        print(f'     {k} tirou {v} no dado')
        sleep(0.5)

print('__-__-'*30)

rkt=('Primeiro lugar','Segundo lugar','Terceiro lugar','Quarto lugar')
cont=0

            # 3 - DEVOLVE DAODS

for pos,c in enumerate(ranking):
        sleep(0.5)
        print(f'     {rkt[cont]}: {c[0]} que tirou {c[1]}')
        cont=cont+1






    
