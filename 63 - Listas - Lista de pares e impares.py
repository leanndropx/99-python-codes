    # - DESCREVENDO O DESAFIO
print('63 - Crie um programa que vai ler vários números e colocar em uma lista.')
print('Depois disso, crie duas listas extras que vão conter apenas os valores pares',end='')
print('e os valores impares digitados, respectivamente.')
print('Ao final, mostre o conteúdo das 3 listas geradas.')
print()


    #INICIALIZANDO O PROGRAMA
    

        # IMPORTA BIBLIOTECAS



            # 1 - RECEBE DADOS

numeros=list()
pares=list()
impares=list()

while True:
    n=int(input('digite um numero: '))
    
            # 2 - MANIPULA DADOS

    if n%2==0:
        pares.append(n)
        numeros.append(n)
    else:
        impares.append(n)
        numeros.append(n)
    pergunta=str(input('gostaria de continuar?: ')).strip().upper()[0]
    while pergunta not in 'SN':
        pergunta=str(input('Não entendi, gostaria de continuar?: ')).strip().upper()[0]
    if pergunta in 'N':
        break

numeros.sort()
pares.sort()
impares.sort()

            
            # 3 - RETORNA DAODS

print(f'lista completa: {numeros}')
print(f'pares: {pares}')
print(f'impares: {impares}')
