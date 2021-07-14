
    # - DESCREVENDO O DESAFIO

print('29 - Faça um programa que leia um número inteiro e diga se ele é ou não um número primo. Um número primo é aquele que só é divisível por 1 e por ele mesmo.')

print()



    #INICIALIZANDO O PROGRAMA
    

        # IMPORTA BIBLIOTECAS



            # 1 - RECEBE DADOS

numero = int(input('digite um número: '))


            # 2 - MANIPULA DADOS, RETORNA DADOS CONFORME CONDICAO

quant=0

for c in range(1,numero+1):

    if numero % c==0:
        print('\033[31m',end=' ')
        quant=quant+1
    
    else:
        print('\033[32m',end=' ')
    print(c, end='')

if quant == 2:
    print('\n\033[m1 - O número {}{}{} é um número primo'.format('\033[31m',numero,'\033[m'))
    print('2 - O número {} foi divisivel apenas {} vezes'.format(numero,quant))

else:
    print('\n\033[mO número {}{}{} não é um número primo'.format('\033[31m',numero,'\033[m'))
    print('O número {} foi divisível {} vezes'.format(numero,quant))









