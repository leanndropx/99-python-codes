    # - DESCREVENDO O DESAFIO
print('84 - Aprimore o desafio 93 para que ele funcione com vários jogadores ',end='')
print('incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador')
print()

    #INICIALIZANDO O PROGRAMA
    

        # IMPORTA BIBLIOTECAS



            # 1 - RECEBE DADOS

jogador=[]
dados={}
gols=[]

soma_gols_da_partida = 0

while True:
        dados['nome'] = str(input('nome do jogador: ')).strip().capitalize()
        dados['quantas_partidas'] = int(input(f'quantas partidas {dados["nome"]} jogou?:  '))

        for partida in range(0, dados['quantas_partidas']):
            gols.append(int(input(f'quantos gols no partida {partida+1}: ')))
            
            soma_gols_da_partida = soma_gols_da_partida + gols[partida]

        dados['soma_gols'] = soma_gols_da_partida
        soma_gols_da_partida = 0
        
        dados['lista_gols'] = gols[:]
        
        gols.clear()
        jogador.append(dados.copy())
        p=str(input('cadastrar mais jogadores?: ')).strip().upper()[0]
        while p not in 'SN':
            p=str(input('ERRO, digite novamente: ')).strip().upper()[0]
        if p in 'N':
            break


    
            # 2 - MANIPULA E CRIA NOVOS DADOS



            
            # 3 - DEVOLVE DAODS

print(f'{"":^4}{"Nome":^20}{"Total":^20}{"Gols":^20}')

for index,jogador in enumerate(jogador):
        
        print(f'{index+1:^4}',end='')
        for key,value in jogador.items():
            if jogador[key] != jogador['quantas_partidas']:
                print(f'{str(value):^20}',end='')
        print()

while True:
        pg = int(input('gostaria de ver os detalhes de qual jogador?'))
        if pg == 999:
            break

        if pg > len(jogador) or pg < 1:
            print(f'\Não existe jogagor com o código {pg}: ')

        else:

            print('-__-'*30)
            print(f'{"":^5}LEVANTAMENTO DO JOGADOR {jogador[pg-1]["nome"]} ')
            for pos,c in enumerate(jogador[pg-1]['gols']):
                print(f'{"":^5}No jogo {pos+1} fez {c} gols')








