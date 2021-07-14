    
    # - DESCREVENDO O DESAFIO
    
print('''09 - Faça um programa que leia um ano qualquer e mostre se ele é ano bissexto. Se o usuário digitar 0, você deverá mostrar o ano atual''')

print()


    #INICIALIZANDO O PROGRAMA
    

        # IMPORTA BIBLIOTECAS

import random
from datetime import date


            # 1 - RECEBE DADOS

ano = int(input('Digite um ano: '))

            
            
            # 2 - MANIPULA/PROCESSA DADOS, RETORNA DADOS CONFORME CONDICIONAL

if ano == 0:
        ano = date.today().year


if ano%4 == 0 and ano%100 != 0 or ano%400 ==0:
        
        print(f'{ano} é um ano bissexto')

else:
        
        print(f'{ano} não é um ano bissexto')







