    # - DESCREVENDO O DESAFIO
print('55 - Desenvolva um programa que leia 4 valores pelo teclado',end='')
print('e guarde-os em uma tupla. No final, mostre:')
print('1 - quantas vezes apareceu o valor 9')
print('2 - em que posição foi digitada o primeiro valor 3')
print('3 - quais foram os números pares')
print()


    #INICIALIZANDO O PROGRAMA
    

        # IMPORTA BIBLIOTECAS



            # 1 - RECEBE DADOS

numeros=(int(input('digite um valor: ')),
        int(input('digite um valor: ')),
        int(input('digite um valor: ')),
        int(input('digite um valor: ')))


            # 2 - MANIPULA, CRIA NOVOS DADOS E RETORNA DADOS CONFORME CONDICIONAL

print('1 - O valor 9 apareceu {} vez'.format(numeros.count(9)))

if 3 in numeros:
        print('2 - O valor 3 foi digitado na posição {}'.format(numeros.index(3)))
else:
        print('2 - O valor 3 não foi digitado')

print(f'3 - Os números pares digitados foram: ',end=' ')


conta_pares=0
for par in numeros:
        if par%2==0:
            conta_pares = conta_pares+1
            print(f'{par},',end=' ')












