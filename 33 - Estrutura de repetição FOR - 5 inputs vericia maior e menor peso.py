
    # - DESCREVENDO O DESAFIO

print('33 - Faça um programa que leia o peso de 5 pessoas.',end='')
print('No final, mostre qual foi o maior e o menor peso lidos')
print()



    #INICIALIZANDO O PROGRAMA
    

        # IMPORTA BIBLIOTECAS

import math

            # 1 - RECEBE DADOS

maior=0
menor=0

for contador in range(1,6):
    peso = float(input('Digite seu peso: '))
    
            # 2 - MANIPULA DADOS

    if contador == 1:
        maior=peso
        menor=peso
    else:
        if peso>maior:
            maior=peso
        if peso<menor:
            menor=peso


            
            # 3 - DEVOLVE DAODS


print('O maior peso é {}'.format(math.trunc(maior)))
print('O menor peso é {}'.format(math.trunc(menor)))
