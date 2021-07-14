    # - DESCREVENDO O DESAFIO
print('58 - Faça um programa que leia 5 valores numéricos e ',end='')
print('guarde-os em uma lista. No final, mostre qual o foi o maior e menor',end='')
print('valor digitados e as suas respectivas posições na lista.')
print()


    #INICIALIZANDO O PROGRAMA
    

        # IMPORTA BIBLIOTECAS



            # 1 - RECEBE DADOS

numeros=list()

for contagem in range(1,6):
        numeros.append(int(input('digite um número: ')))

    
            # 2 - MANIPULA E CRIA NOVOS DADOS

maior=max(numeros)
menor=min(numeros)
index_maior = numeros.index(maior)
index_menor = numeros.index(menor)

            
            # 3 - DEVOLVE DAODS

print('1 - O maior valor digitado foi {}, na posição {} '.format(maior,index_maior+1))
print('2 - O menor valor digitado foi {}, na posição {}'.format(menor,index_menor+1))







