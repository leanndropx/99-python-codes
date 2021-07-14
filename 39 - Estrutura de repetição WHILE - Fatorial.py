
    # - DESCREVENDO O DESAFIO

print('39 - Faça um programa que leia um número qualquer e mostre o seu fatorial')
print()



    #INICIALIZANDO O PROGRAMA
    

        # IMPORTA BIBLIOTECAS

from math import factorial

            # 1 - RECEBE DADOS

n=int(input('digite o número: '))
contador=n
fatorial=1


            # 2 - MANIPULA E CRIA NOVOS DADOS

while contador>0:
        print(contador,end=' ')
        print(' x ' if contador>1 else ' = ',end='')
        fatorial=fatorial*contador
        contador=contador-1


            # 3 - DEVOLVE DAODS

print(f'\033[35m O fatorial de {n} é {fatorial}')
print(f'calculando de outra maneira, com a função factorial: {factorial(n)}')
