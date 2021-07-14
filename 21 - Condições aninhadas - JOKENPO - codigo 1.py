
    # - DESCREVENDO O DESAFIO

print('21 - Crie um programa que faça o computador jogar \033[4mJOKENPO\033[m')
print()




    #INICIALIZANDO O PROGRAMA

print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO')
sleep(0.5)


        # IMPORTA BIBLIOTECAS

import random
from time import sleep


            # 1 - RECEBE DADOS

escolha=['pedra','papel','tesoura']
computador=random.randint(0,2)
jogador=int(input('''[ 0 ] - PEDRA
[ 1 ] - PAPEL
[ 2 ] - TESOURA
escolha sua opção: '''))

    
            # 2 - MANIPULA E RETORNA DADOS CONFORME CONDICIONAL


print('O computador jogou {}'.format(escolha[computador]))
print('Você jogou {}'.format(escolha[jogador]))

if computador==0:
    if jogador==0:
        print('DEU EMPATE')
    if jogador==1:
        print('VOCE VENCEU')
    if jogador==2:
        print('VOCE PERDEU')

if computador==1:
    if jogador==0:
        print('VOCE PERDEU')
    if jogador==1:
        print('DEU EMPATE')
    if jogador==2:
        print('VOCE VENCEU')

if computador==2:
    if jogador==0:
        print('VOCE VENCEU')
    if jogador==1:
        print('VOCE PERDEU')
    if jogador==2:
        print('DEU EMPATE')
