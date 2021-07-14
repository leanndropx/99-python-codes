    # - DESCREVENDO O DESAFIO
print('61 - Crie um programa onde o usuário possa digitar 5 valores numéricos ',end='')
print('e cadastre-os em uma lista, já na posição correta de inserção, sem usar o sort')
print('No final, mostre a lista ordenada na tela.')
print()

    #INICIALIZANDO O PROGRAMA
    

        # IMPORTA BIBLIOTECAS



            # 1 - RECEBE DADOS

lista_de_numeros = list()

for contagem in range(0,5):
        
        numero = int(input('digite um valor: '))
        
        
            # 2 - MANIPULA E CRIA NOVOS DADOS

        if contagem == 0:
            lista_de_numeros.append(numero)
        
        elif numero >= lista_de_numeros[-1]:
            lista_de_numeros.append(numero)
        
        else:
            for posicao in range(0,len(lista_de_numeros)):
                if numero <= lista_de_numeros[posicao]:
                    lista_de_numeros.insert(posicao,numero)
                    break

            
            # 3 - DEVOLVE DAODS

print(f'lista ordenada: {lista_de_numeros}')






