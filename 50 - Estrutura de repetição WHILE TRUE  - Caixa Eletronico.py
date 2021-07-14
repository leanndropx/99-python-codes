    # - DESCREVENDO O DESAFIO
print('50 - Crie um programa que simule o funcionamento de um caixa eletrônico. ',end='')
print('No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro',end=' ')
print('e o programa vai informar quantas cédulas de cada valor serão entregues.')
print('         > Considere que o programa possui cedulas de 50, 20, 10 e 1 real')
print()



    #INICIALIZANDO O PROGRAMA
    

        # IMPORTA BIBLIOTECAS



            # 1 - RECEBE DADOS

cedulas_50=0
cedulas_20=0
cedulas_10=0
cedulas_1=0

while True:
        print('\033[7m     \033[31mSEJA BEM-VINDO AO BANCO LPX     \033[m')
        print('  ')
        valor=int(input('qual o valor do saque?  R$ '))
        
                # 2 - MANIPULA E CRIA NOVOS DADOS

        if valor>=50:
            cedulas_50=valor//50
            sobra=valor%50
            if sobra>=20:
                cedulas_20=sobra//20
                sobra=sobra%20
            if sobra>=10 and sobra<20:
                cedulas_10=sobra//10
                sobra=sobra%10
            if sobra<10:
                cedulas_1=sobra

        elif valor<50 and valor>=20:
            cedulas_20=valor//20
            sobra=valor%20
            if sobra>=10:
                cedulas_10=sobra//10
                sobra=sobra%10
            if sobra<10:
                cedulas_1=sobra

        elif valor<20 and valor>=10:
            cedulas_10=valor//10
            sobra=valor%10
            cedulas_1=sobra

        elif valor<10:
            cedulas_1=valor//1
                
                # 3 - DEVOLVE DAODS

        if cedulas_50!=0:
            print('cédulas de 50: {}{}{}'.format('\033[35m',cedulas_50,'\033[m'))
            cedulas_50=0
        if cedulas_20!=0:
            print('cédulas de 20: {}{}{}'.format('\033[35m',cedulas_20,'\033[m'))
            cedulas_20=0
        if cedulas_10!=0:
            print('cédulas de 10: {}{}{}'.format('\033[35m',cedulas_10,'\033[m'))
            cedulas_10=0
        if cedulas_1!=0:
            print('cédulas de 1: {}{}{}'.format('\033[35m',cedulas_1,'\033[m'))
            cedulas_1=0
        if valor==0:
            break
        print('  ')


print(' ')
print('\033[7m     VOLTE SEMPRE AO \033[31mBANCO LPX        \033[m')







