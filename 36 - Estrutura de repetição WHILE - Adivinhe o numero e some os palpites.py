
    # - DESCREVENDO O DESAFIO

print('36 - Melhore o jogo do desafio 28, onde o computador vai pensar em um número entre 0 e 10',end='')
print('Só que agora o jogador vai tentar adivinhar até acertar ',end='')
print('mostrando no final quantos palpites foram necessários para vencer')
print()



    #INICIALIZANDO O PROGRAMA
    

        # IMPORTA BIBLIOTECAS

import random

            # 1 - RECEBE DADOS

computador=random.randint(0,50)
acertou=False
tentativas=0
    
            # 2 - MANIPULA E CRIA NOVOS DADOS

print('O computador escolheu um número')
print('Vamos ver se você consegue adivinhar')

while not acertou:
    jogador=int(input('Qual é o seu palpite?: '))
    
    if jogador==computador:
        acertou=True
    else:
        tentativas=tentativas+1
        if jogador<computador:
            print('O número é maior')
        else:
            print('O número é menor')

            
            # 3 - DEVOLVE DAODS

print('Acertou. Foram {} tentativas, {}{}{} erradas e {} certa'.format(tentativas+1,'\033[31m',tentativas,'\033[m',1))







