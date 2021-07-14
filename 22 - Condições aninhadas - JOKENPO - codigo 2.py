
    # - DESCREVENDO O DESAFIO

print('22 - Crie um programa que faça o computador jogar \033[4mJOKENPO\033[m')

print()




    #INICIALIZANDO O PROGRAMA

        #IMPORTA BIBLIOTECAS

import random

    
            #  1 - RECEBE DADOS
        
opcoes_para_escolher = ['pedra','papel','tesoura']
jogador_escolheu = input('Digite sua escolha: pedra, papel ou tesoura: ').strip().lower()
computador_escolheu = random.choice(opcoes_para_escolher)

        


            #  2 - MANIPULA E RETORNA DADOS DIFERENTES PARA CADA CONDICAO DECLARADA


if jogador_escolheu == computador_escolheu: #2
    
        print(f'O computador também escolheu {computador_escolheu}, DEU EMPATE')
  
  

elif jogador_escolheu != computador_escolheu and jogador_escolheu == 'pedra' and computador_escolheu == 'papel':
    
        print(f'Você perdeu jogador, o computador escolheu {computador_escolheu}.')


elif jogador_escolheu != computador_escolheu and jogador_escolheu == 'pedra' and computador_escolheu == 'tesoura':
    
        print(f'1 - PARABENS JOGADOR, VOCE GANHOU. O computador escolheu {computador_escolheu}')


elif jogador_escolheu != computador_escolheu and jogador_escolheu == 'papel' and computador_escolheu == 'pedra':
    
        print(f'1 - PARABENS JOGADOR, VOCE GANHOU. O computador escolheu {computador_escolheu}')


elif jogador_escolheu != computador_escolheu and jogador_escolheu == 'papel' and computador_escolheu == 'tesoura':
    
        print(f'Você perdeu jogador, o computador escolheu {computador_escolheu}.')


elif jogador_escolheu != computador_escolheu and jogador_escolheu == 'tesoura' and computador_escolheu == 'pedra':
    
        print(f'Você perdeu jogador, o computador escolheu {computador_escolheu}.')


elif jogador_escolheu != computador_escolheu and jogador_escolheu == 'tesoura' and computador_escolheu == 'papel':
    
        print(f'1 - PARABENS JOGADOR, VOCE GANHOU. O computador escolheu {computador_escolheu}')


else:
        print('opção não identificada')
