    # - DESCREVENDO O DESAFIO
print('60 - Crie um programa onde o usuário possa digitar vários ',end='')
print('valores numéricos e cadastre-os em uma lista. Caso o número já exista',end=' ')
print('lá dentro, ele não será adicionado. No final, serão exibidos todos os',end=' ')
print('valores únicos digitados, em ordem crescente')
print()


    #INICIALIZANDO O PROGRAMA
    

        # IMPORTA BIBLIOTECAS



            # 1 - RECEBE DADOS

valores=list()
mostra_valores_repetidos=list()

while True:

        n=int(input('digite um valor: '))
        
                    # 2 - MANIPULA E CRIA NOVOS DADOS

        if n not in valores:
            valores.append(n)
            print('Valor adicionado a lista com sucesso.')
        
        else:
            mostra_valores_repetidos.append(n)
            print('Este valor já existe na lista, por isso não foi adicionado')

        deseja_continuar = str(input('gostaria de continuar?: ')).strip().upper()[0]
        
        if deseja_continuar in 'N':
            break
        
        while deseja_continuar not in 'SN':
            deseja_continuar = str(input('não entendi, digite novamente: ')).strip().upper()[0]
                
            # 3 - DEVOLVE DAODS


print(f'1 - Os valores não repetidos adicionados a lista foram: {sorted(valores)}')
print(f'2 - Os valores repetidos digitados foram: {mostra_valores_repetidos}.')
