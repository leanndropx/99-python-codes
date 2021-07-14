
    # - DESCREVENDO O DESAFIO

print('''11 - Escreva um programa que pergunte o salário de um funcionário e calcule o valor de seu aumento.
            1 - Para salários superiores a R$1250,00, calcule um aumento de 10%
            2 - Para os inferiores ou iguais, o aumento é de 15%''')

print()

    #INICIALIZANDO O PROGRAMA
    

        # IMPORTA BIBLIOTECAS

import math
import random


            # 1 - RECEBE DADOS

salario = float(input('Digite seu salário'))

    
            # 2 - MANIPULA DAODS

aumento_10_porcento = (salario * 0.1) + salario
aumento_15_porcento = (salario * 0.15) + salario

            
            # 3 - DEVOLVE DAODS, CONFORME CONDICIONAL


print()

if salario>1250:
    
        print(f'1 - Seu salário é R$ {salario:.2f}.')
    
        print('2 - Então, seu aumento será de 10%, o que equivale um total de R$ {:.2f} reais'.format(salario*0.1))
    
        print('3 - Logo, R$ {:.2f} será seu novo salário'.format(aumento_10_porcento))


else:
        print('1 - Seu salarário é R$ {:.2f}'.format(salario))
    
        print('2 - Então, seu aumento será de 15%, um total de R$ {:.2f} reais'.format(salario*0.15))
    
        print('3 - Logo, seu novo salário, com aumento, será {:.2f}'.format(aumento_15_porcento))

