    
    # - DESCREVENDO O DESAFIO

print('''10 - Faça um programa que leia 3 numeros e mostre qual é o maior e qual é o menor''')

print()

    #INICIALIZANDO O PROGRAMA
    

        # IMPORTA BIBLIOTECAS

import random


            # 1 - RECEBE DADOS

primeiro_numero = int(input('Primeiro numero: '))
segundo_numero = int(input('Segundo numero: '))
terceiro_numero = int(input('Terceiro numero: '))

    
            # 2 - MANIPULA E CRIA NOVOS DADOS


#MENOR
if primeiro_numero < segundo_numero and primeiro_numero < terceiro_numero:
        menor = primeiro_numero

if segundo_numero < primeiro_numero and segundo_numero < terceiro_numero:
        menor = segundo_numero

if terceiro_numero < primeiro_numero and terceiro_numero < segundo_numero:
        menor = terceiro_numero


#MAIOR
if primeiro_numero > segundo_numero and primeiro_numero > terceiro_numero:
        maior = primeiro_numero

if segundo_numero > primeiro_numero and segundo_numero > terceiro_numero:
        maior = segundo_numero

if terceiro_numero > primeiro_numero and terceiro_numero > segundo_numero:
        maior = terceiro_numero


            # 3 - DEVOLVE DAODS

print()
print(f'1 - O menor número é {menor}.')
print(f'2 - O maior número é {maior}.')








