    # - DESCREVENDO O DESAFIO
print('56 - Crie um programa que tenha uma tupla única com nome de produtos ',end='')
print('e seus respectivos preços, na sequência. No final, mostre uma listagem de preços',end=' ')
print('organizando os dados em forma tabular')
print()

    #INICIALIZANDO O PROGRAMA
    

        # IMPORTA BIBLIOTECAS



            # 1 - RECEBE DADOS

produtos=('Caneta',3.50,
          'Lapis',4,
          'Estojo',5.50,
          'Camiseta',23,
          'Mochila',150,
          'Carro',35000)

    
            # 2 - MANIPULA DADOS, RETORNA DADOS


print('_-_'*14)
print(f'{"LISTAGEM DE PREÇOS":^35}')
print('_-_'*14)

for mosta_index, mostra_valor in enumerate(produtos):
        
        if mosta_index % 2 == 0:
            print(f'{mostra_valor:.<30}',end='')
        else:
            print(f'R${mostra_valor:>10.2f}')




#OUTRA OPCAO DE CODIGO
print()

print('*.*'*14)
print(f'{"LISTA DE PRODUTOS E PRECOS":^40}')
print('*.*'*14)

for numero in range(0,len(produtos)):
        if numero%2==0:
            print(f'{produtos[numero]:.<30}',end=' ')
        else:
            print(f'R${produtos[numero]:>10.2f}')
