
    # - DESCREVENDO O DESAFIO

print('47 - Faça um programa que jogue PAR ou IMPAR com o computador. ',end='')
print('O jogo só será interrompido quando o jogador perder,',end='')
print('mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.')
print()


    #INICIALIZANDO O PROGRAMA
    

        # IMPORTA BIBLIOTECAS

import random

            # 1 - RECEBE DADOS

v=0
while True:
    
    computador=random.randint(0,10)
    jogador=int(input('escolha um número: '))
    escolha=str(input('você quer par ou impar?: ')).strip().upper()[0]

            # 2 - MANIPULA, CRIA NOVOS DADOS E RETORNA VALORES CONFORME CONDICIONAL

    soma=jogador+computador

    while escolha not in 'PI':
        escolha=str(input('opção inválida. Escolha P ou I: ')).strip().upper()
    print(f'O jogador escolheu {jogador} e o computador escolheu {computador}')

    print('DEU PAR' if soma%2==0 else 'DEU IMPAR')

    if soma%2==0 and escolha=='P':
        print(f'A soma foi {soma} e voce venceu')
        v=v+1
    elif soma%2==0 and escolha=='I':
        print(f'A soma foi {soma} e você perdeu')
        break
    elif soma%2!=0 and escolha=='P':
        print(f'A soma foi {soma} e você perdeu')
        break
    elif soma%2!=0 and escolha=='I':
        print(f'A soma foi {soma} e você venceu')
        v=v+1

print(f'O número de vitórias foi {v}')










