    # - DESCREVENDO O DESAFIO
print('73 - Faça um programa que ajude um jogador da mega sena a gerar palpites.')
print('O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números ',end='')
print('entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.')
print()

    #INICIALIZANDO O PROGRAMA
    

        # IMPORTA BIBLIOTECAS

from random import randint
from time import sleep


            # 1 - RECEBE DADOS

lista_faz_um_jogo = list()
lista_todos_jogos = list()

total_de_jogos = int(input('quantos jogos?: '))

    
            # 2 - MANIPULA DADOS

print(f'{"SORTEANDO JOGOS":^40}')
sleep(0.5)

for jogo in range(0,total_de_jogos):

        for palpite in range(0,6):
            numero = randint(1,60)
            
            while numero in lista_faz_um_jogo:
                numero = randint(1,60)
            lista_faz_um_jogo.append(numero)

        lista_faz_um_jogo.sort()
        lista_todos_jogos.append(lista_faz_um_jogo[:])
        
        lista_faz_um_jogo.clear()

                
                # 3 - RETORNA DAODS

        print(f'Palpite {jogo+1}: {lista_todos_jogos[jogo]}')
        sleep(0.5)

print('{:^40}'.format('BOA SORTE'))
