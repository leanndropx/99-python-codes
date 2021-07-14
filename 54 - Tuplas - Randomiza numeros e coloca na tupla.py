    # - DESCREVENDO O DESAFIO
print('54 - Crie um programa que vai gerar 5 numeros aleatórios ',end='')
print('e colocar em uma tupla. Depois disso, mostre a listagem de números gerados',end='')
print('e também indique o menor e maior valor que estão na tupla.')
print()



    # - INICIALIZANDO O PROGRAMA
    

        # IMPORTA BIBLIOTECAS

from random import randint

            # 1 - RECEBE DADOS

numeros=(randint(0,9),randint(0,9),randint(0,9),
         randint(0,9),randint(0,9))

    
            # 2 - MANIPULA DADOS, RETORNA DADOS

print('Os números sorteados foram: ',end=' ')
for cada in numeros:
    print(f'{cada}',end=' ')

print('\nO maior valor foi {}'.format(max(numeros)))
print('O menor valor foi {}'.format(min(numeros)))










