
    # - DESCREVENDO O DESAFIO

print('20 - Elabore um programa que calcule o valor a ser pago por um produto considerando',end='')
print('o seu preço normal e condição de pagamento:')

print('1 - A vista no dinheiro/cheque: 10% de desconto')
print('2 - A vista no cartão: 5% de desconto')
print('3 - em até 2x no cartão: preço normal')
print('4 - 3x ou mais no cartão: 20% de juros')

print()



    #INICIALIZANDO O PROGRAMA
    

        # IMPORTA BIBLIOTECAS

import random

            # 1 - RECEBE DADOS

preco = float(input('Digite o preço do produto: '))


print()
print('O valor original do produto é R$ {:.2f} reais'.format(preco))
print()


forma_de_pagamento = float(input('Selecione uma das formas de pagamento apresentadas acima: ').strip())


            # 2 - MANIPULA DADOS, CRIA NOVOS DADOS, RETORNA DADOS CONFORME CONDICAO
            

if forma_de_pagamento == 1:
    print('1 - Você escolheu a opção DINHEIRO/CHEQUE, então:')
    
    preco_com_desconto = preco - (preco*0.1)
    print('2 - Você tem 10% de desconto, logo:')
    print('3 - O produto vai te custar R${:.2f} '.format(preco_com_desconto))


elif forma_de_pagamento == 2:
    
    print('1 - Você escolheu a opção de pagamento A VISTA NO CARTAO')
    print('2 - Então, você tem 5% de desconto')
    preco_com_desconto = preco - (preco*0.05)
    
    print('3 - Logo, o produto que custaria R${}'.format(preco))
    print('4 - Vai custar {}'.format(preco_com_desconto))


elif forma_de_pagamento == 3:
    print('1 - Você escolheu a opção em até 2 X no cartão, então:')
    print('2 - Você não tem desconto, logo:')
    print('3 - O produto vai te custar o preço original: {:.2f}'.format(preco))


elif forma_de_pagamento == 4:
    print('1 - opção escolhida: 3 x ou mais no cartão')
    print('2 - Logo, haverá um acréscimo de 20% de juros')
    
    preco_com_juros = (preco*0.2) + preco
    print('3 - Então, o produto vai te custar R${}{:.2f}{}'.format('\033[4m',preco_com_juros,'\033[m'))

else:
    print('\033[1;7;31mOPCAO NAO EXISTENTE\033[m')






