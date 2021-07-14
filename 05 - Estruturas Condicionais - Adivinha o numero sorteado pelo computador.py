# - DESCREVENDO O DESAFIO

print('''05 - Escreva um programa que faça o computador pensar em um numero inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu''')
    
    
    #INICIALIZANDO O PROGRAMA

import random
import time
    
        # 1 - RECEBE DADOS

computador=int(random.randint(0,5))
jogador=int(input('Jogador, escolha um número = '))

        
        # 2 - MANIPULA E CRIA NOVOS DADOS
        
if jogador==computador:
    jogador_venceu = True
        
        
        # 3 - DEVOLVE DADOS, NESTE CASO RESPEITANDO UMA CONDIÇAO

print('PROCESSANDO...')
time.sleep(2)

if jogador_venceu:
    print('Parabéns, você acertou o número escolhido pelo computador e venceu o jogo!')
else:
    print(f'Você perdeu jogador. O número escolhido pelo computador foi {computador} !')
