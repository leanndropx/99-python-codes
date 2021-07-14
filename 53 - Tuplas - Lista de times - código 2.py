    # - DESCREVENDO O DESAFIO
print('53 - Crie uma tupla preenchida com os 20 primeiros colocados',end='')
print('do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre: ')
print('1 - apenas os 5 primeiros colocados')
print('2 - os ultimos colocados da tabela')
print('3 - uma lista com os times em ordem alfabética')
print('4 - em que posição na tabela está o time Chapecoense')
print()



    #INICIALIZANDO O PROGRAMA
    

        # IMPORTA BIBLIOTECAS



            # 1 - RECEBE DADOS

ranking=('Palmeiras','Santos','Vasco da Gama','Grêmio','Flamengo','Corinthians',
          'Internacional','Cruzeiro','São Paulo','Atletico Mineiro','Botafogo',
          'Fluminense','Curitiba','Bahia','Goais','Guarani','Sport','Portuguesa',
          'Atletico Paranaense','Vitoria')


    
            # 2 - MANIPULA DADOS, RETORNA DADOS

print()
print('1 - Os 5 primeiros colocados foram: ',end=' ')

for cont in ranking[0:5]:
    print(cont,end='')
    print(',' if cont>ranking[4] else ' ',end=' ')

print('\n2 - Os 4 últimos colocados foram: ',end=' ')

for cont in ranking[-1:-10:-1]:
    print(cont,end=' ')
    print(', ' if cont!=ranking[-9] else ' ',end='')

print(f'\n3 - a lista em ordem alfabetica: {sorted(ranking)}')
print(f'4 - O Curitiba está na posição {ranking.index("Curitiba")+1}')
