    # - DESCREVENDO O DESAFIO
print('62 - Crie um programa que vai ler vários números e colocar em uma lista')
print('Depois disso, mostre:')
print('1 - quantos números foram digitados')
print('2 - a lista de valores, ordenada de forma decrescente')
print('3 - se o valor 5 foi digitado e está ou não na lista')
print('  ')


    #INICIALIZANDO O PROGRAMA
    

        # IMPORTA BIBLIOTECAS



            # 1 - RECEBE DADOS

lista_de_numeros=list()
deseja_continuar ='S'



while deseja_continuar == 'S':

        lista_de_numeros.append(int(input('digite um valor: ')))
        
        deseja_continuar = str(input('gostaria de continuar?: ')).strip().upper()[0]
        
        while not deseja_continuar in 'SN':
            deseja_continuar = str(input('Não entendi, digite novamente: ')).strip().upper()[0]

    
            # 2 - MANIPULA E CRIA NOVOS DADOS

lista_de_numeros.sort(reverse=True)
quantidade_de_numeros = len(lista_de_numeros)

            # 3 - DEVOLVE DAODS

print(f'1 - foram digitados {quantidade_de_numeros} números')
print(f'2 - a lista em ordem descrescente: {lista_de_numeros}')
if lista_de_numeros.count(5)==0:
        print('3 - O valor 5 não foi digitado nenhuma vez')
else:
        print(f'3 - O valor 5 foi digitado {lista_de_numeros.count(5)} {"vez" if lista_de_numeros.count(5)==1 else "vezes"}')








