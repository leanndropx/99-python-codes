    # - DESCREVENDO O DESAFIO
print('67 - Faça um programa que leia nome e peso de várias pessoas',end='')
print('guardando tudo em uma lista. No final, mostre: ')
print('1 - quantas pessoas foram cadastradas.')
print('2 - uma listagem com as pessoas mais pesadas')
print('3 - uma listagem com as pessoas mais leves')
print()

    #INICIALIZANDO O PROGRAMA
    

        # IMPORTA BIBLIOTECAS

import math

            # 1 - RECEBE DADOS

pessoas=list()
dados=list()
pesos=list()
maior=0
menor=0

while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))

    deseja_continuar = str(input('deseja cadastrar mais dados?: ')).strip().upper()[0]
    while p not in 'SN':
        deseja_continuar = str(input('\033[31merro, digite novamente [S/N]\033[m')).strip().upper()[0]


    
            # 2 - MANIPULA E CRIA NOVOS DADOS

    pessoas.append(dados[:])
    pesos.append(dados[:][1])


    dados.clear()
    if p in 'N':
        break

pessoas.sort(reverse=True)

            
            # 3 - DEVOLVE DAODS

print(f'1 - Foram cadastradas {len(pessoas)} pessoas na lista')
print(f'2 - pessoas mais pesadas: {pesos}')
print(f'3 - Os \033[35m{(math.ceil(len(pessoas)/2))}\033[m maiores pesos foram: {pesos[0:math.ceil(len(pessoas)/2)]} ')
print(f'4 - Os {math.trunc(len(pessoas)/2)} pesos mais leves foram: {pesos[-1*(math.trunc(len(pessoas)/2)):]}')









