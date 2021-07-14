
    # - DESCREVENDO O DESAFIO

print('37 - Crie um programa que leia DOIS valores e mostre um menu na tela:')
print('1 - somar')
print('2 - multiplicar')
print('3 - maior')
print('4 - novos números')
print('5 - sair do programa')
print()
print()


    # - INICIALIZANDO O PROGRAMA
    

        # IMPORTA BIBLIOTECAS

from time import sleep

            # 1 - RECEBE DADOS

n1=int(input('digite o primeiro número: '))
n2=int(input('digite o segundo número: '))
print('O que você gostaria de fazer: ')

opcao=0
while opcao!=5:
    print('\033[7m','                                             ','\033[m')
    print('''                [ 1 ] Somar
                [ 2 ] Multiplicar
                [ 3 ] Maior
                [ 4 ] Novos números
                [ 5 ] Sair do programa''')
    print('\033[7m', '                                             ', '\033[m')
    opcao=int(input('escolha a opção: '))


    
            # 2 - MANIPULA E CRIA NOVOS DADOS

    if opcao==1:
        soma=n1+n2
        print('A soma é {}'.format(soma))

    elif opcao==2:
        multiplicar=n1*n2
        print('O produto é {}'.format(multiplicar))

    elif opcao==3:
        if n1>n2:
            maior=n1
        else:
            maior=n2
        print('O maior número é {}'.format(maior))

    elif opcao==4:
        n1=int(input('digite o primeiro número: '))
        n2=int(input('digite o segundo número: '))

    elif opcao==5:
        print('Finalizando...')


    else:
        print('opção inválida')

    print()
    sleep(1)


print('O programa foi encerrado!')
            
            # 3 - DEVOLVE DAODS









