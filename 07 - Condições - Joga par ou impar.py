    # - DESCREVENDO O DESAFIO

print('''07 - Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR''')

    
    
    #INICIALIZANDO O PROGRAMA

import random
            
            # 1 - RECEBE DADOS

numero_sorteado = random.randint(0,2000)

            
            # 2 - MANIPULA DADOS E CRIA NOVOS DADOS
            
verifica_par = numero_sorteado % 2

            
            # 3 - RETORNA DADOS

print()
print(f'O número sorteado foi {numero_sorteado} e é ',end='')

if verifica_par == 0:
    
        print('um número PAR')
else:
    
        print('um número IMPAR')
