    # - DESCREVENDO O DESAFIO
print('52 - Crie uma tupla preenchida com os 20 primeiros colocados',end='')
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


    
            # 2 - MANIPULA E CRIA NOVOS DADOS

# ESTE PROGRAMA APENAS RETORNA DADOS

            
            # 3 - DEVOLVE DAODS


#opcao de código 1
print('  ')
print(f'1 - Os cinco primeiros colocados são: {ranking[0]}, {ranking[1]}, {ranking[2]}, {ranking[3]} e {ranking[4]}')
print(f'2 - Os 4 últimos colocados são: {ranking[-1]}, {ranking[-2]}, {ranking[-3]} e {ranking[-4]}')
print(f'3 - Lista em ordem alfabética: {sorted(ranking)}')
print(f'4 - O Cruzeiro está na posição {ranking.index('Cruzeiro')}'.)

