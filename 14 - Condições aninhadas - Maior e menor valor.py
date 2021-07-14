
    # - DESCREVENDO O DESAFIO

print('14 - Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela',end='')
print('uma mensagem: ')
print('1 - O primeiro valor é maior')
print('2 - O segundo valor é maior')
print('3 - Não existe valor maior, os dois são iguais')


    #INICIALIZANDO O PROGRAMA
    

        # IMPORTA BIBLIOTECAS

import random

            # 1 - RECEBE DADOS

primeiro_numero = int(input('Primeiro número: '))
segundo_numero = int(input('Segundo número: '))

    
            # 2 - MANIPULA E CRIA NOVOS DADOS

if primeiro_numero > segundo_numero and primeiro_numero != segundo_numero:
        print('O primeiro valor {}{}{} é maior'.format('\033[32m',primeiro_numero,'\033[m'))


elif primeiro_numero < segundo_numero and primeiro_numero != segundo_numero:
        print('O segundo valor é maior')


elif primeiro_numero == segundo_numero:
        print('Não existe valor maior, os dois são iguais')










