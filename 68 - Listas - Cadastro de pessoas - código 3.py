    # - DESCREVENDO O DESAFIO
print('68 - Faça um programa que leia nome e peso de várias pessoas',end='')
print('guardando tudo em uma lista. No final, mostre: ')
print('1 - quantas pessoas foram cadastradas.')
print('2 - uma listagem com as pessoas mais pesadas')
print('3 - uma listagem com as pessoas mais leves')
print()

    #INICIALIZANDO O PROGRAMA
    

        # IMPORTA BIBLIOTECAS

from math import ceil
from math import trunc


            # 1 - RECEBE DADOS

temp=list()
princ=list()
maior=menor=0

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('peso: ')))

    
            # 2 - MANIPULA E CRIA NOVOS DADOS

    if len(princ)==0:
        maior=menor=temp[1]
    else:
        if temp[1]>maior:
            maior=temp[1]
        if temp[1]<menor:
            menor=temp[1]
    princ.append(temp[:])
    temp.clear()
    p=str(input('mais cadastros?: ')).strip().upper()[0]
    while p not in 'SN':
        p=str(input('\033[31mERRO, digite S ou N:\033[m ')).strip().upper()[0]
    if p=='N':
        break
            
            # 3 - DEVOLVE DAODS

print('Foram cadastrados {} pesos'.format(len(princ)))
print('Os {} maiores pesos foram de: '.format(ceil(len(princ)-1)),end='')
for c in princ:
    if c[1]!=menor:
        print(f'{c[0]}, ',end='')

print('\nO menor peso foi de: '.format(trunc(menor)),end='')
for c in princ:
    if c[1]==menor:
        print(f'{c[0]}, ')

print(princ)








