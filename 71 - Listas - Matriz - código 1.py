    # - DESCREVENDO O DESAFIO
print('71 - Crie um programa que crie uma matriz de dimensão 3 x 3',end=' ')
print('e preencha com valores lidos pelo teclado.')
print('No final, mostre a matriz na tela com a formatação correta')
print()

    #INICIALIZANDO O PROGRAMA
    

        # IMPORTA BIBLIOTECAS



            # 1 - RECEBE DADOS

matriz=[[0,0,0],[0,0,0],[0,0,0]]

for linha in range(0,3):
        for coluna in range(0,3):
            matriz[linha][coluna]=int(input(f'digite o valor {linha},{coluna}: '))

    
            # 2 - MANIPULA DADOS, RETORNA DADOS

for linha in range(0,3):
        for coluna in range(0,3):
            print(f'[{matriz[linha][coluna]:^5}]',end=' ')
        print()










