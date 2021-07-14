    # - DESCREVENDO O DESAFIO
print('66 - Faça um programa que leia nome e peso de várias pessoas',end='')
print('guardando tudo em uma lista. No final, mostre: ')
print('1 - quantas pessoas foram cadastradas.')
print('2 - uma listagem com as pessoas mais pesadas')
print('3 - uma listagem com as pessoas mais leves')
print()

    #INICIALIZANDO O PROGRAMA
    

        # IMPORTA BIBLIOTECAS



            # 1 - RECEBE DADOS

lista_temporaria = list()
lista_nome_pesos = list()
maior=menor=0

while True:
        lista_temporaria.append(str(input('Nome: ')))
        lista_temporaria.append(int(input('Peso: ')))
        
                # 2 - MANIPULA E CRIA NOVOS DADOS

        if len(lista_nome_pesos)==0:
            maior=lista_temporaria[1]
            menor=lista_temporaria[1]
        
        else:
            if lista_temporaria[1] > maior:
                maior=lista_temporaria[1]
            
            if lista_temporaria[1] < menor:
                menor=lista_temporaria[1]

        lista_nome_pesos.append(lista_temporaria[:])
        lista_temporaria.clear()
        
        
        deseja_continuar = str(input('mmais pessoas?: ')).strip().upper()[0]
        
        while deseja_continuar not in 'SN':
            deseja_continuar = str(input('ERRO, digite de novo: ')).strip().upper()[0]
        
        if deseja_continuar == 'N':
            break


            
            # 3 - DEVOLVE DAODS


print(f'Foram cadastradas {len(lista_nome_pesos)} pessoas')
print(f'maior peso: {maior} de: ',end='')
for pessoa in lista_nome_pesos:
        if pessoa[1]==maior:
            print(pessoa[0])

print(f'menor peso: {menor} de: ',end='')
for pessoa in lista_nome_pesos:
            if pessoa[1]==menor:
                print(pessoa[0])


