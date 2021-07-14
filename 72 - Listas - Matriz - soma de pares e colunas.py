    # - DESCREVENDO O DESAFIO
print('72 - Aprimore o desafio anterior, mostrando no final:')
print('1 - a soma de todos os valores pares digitados')
print('2 - a soma dos valores da terceira coluna')
print('3 - o maior valor da segunda linha')
print()

    #INICIALIZANDO O PROGRAMA
    

        # IMPORTA BIBLIOTECAS



            # 1 - RECEBE DADOS

numeros=[[0,0,0],[0,0,0],[0,0,0]]

soma_pares=0
soma_coluna=0
maior=0

for linha in range(0,3):
        for coluna in range(0,3):
            numeros[linha][coluna]=int(input(f'digite o número {linha} , {coluna}: '))


                # 2 - MANIPULA DADOS,RETORNA DADOS

            if numeros[linha][coluna]%2==0:
                soma_pares=soma_pares+numeros[linha][coluna]
            if linha==numeros[1] and coluna==numeros[0]:
                maior=numeros[1][0]
            else:
                if numeros[1][coluna]>maior:
                    maior=numeros[1][coluna]

for linha in range(0,3):
        soma_coluna = soma_coluna + numeros[linha][1]
        
        for coluna in range(0,3):
            print(f'[{numeros[linha][coluna]:^7}]',end=' ')
        print()


print(f'soma dos numeros pares: {soma_pares}')
print(f'soma dos numeros da segunda coluna: {soma_coluna}')
print(f'maior valor da segunda liha: {maior}')

