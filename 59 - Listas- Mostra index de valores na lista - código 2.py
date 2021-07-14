    # - DESCREVENDO O DESAFIO
print('59 - Faça um programa que leia 5 valores numéricos e ',end='')
print('guarde-os em uma lista. No final, mostre qual o foi o maior e menor',end='')
print('valor digitados e as suas respectivas posições na lista.')
print()


    #INICIALIZANDO O PROGRAMA
    

        # IMPORTA BIBLIOTECAS



            # 1 - RECEBE DADOS

valores=list()

maior=0
menor=0
for posicao in range(0,5):
        valores.append(int(input(f'digite um valor na posição {posicao}: ')))

                # 2 - MANIPULA E CRIA NOVOS DADOS

        if posicao==0:
            maior=valores[posicao]
            menor=valores[posicao]
        else:
            if valores[posicao]>maior:
                maior=valores[posicao]
            if valores[posicao]<menor:
                menor=valores[posicao]


            
            # 3 - DEVOLVE DAODS

print(f'O maior valor digitado foi {maior} {"na posição" if valores.count(maior)==1 else "nas posições"}: ',end=' ')

for mostra_index ,mostra_valor in enumerate(valores):
        if mostra_valor == maior:
            print(f'{mostra_index + 1}, ',end=' ')

print(f'\nO menor valor digitado foi {menor} {"na posição" if valores.count(menor)==1 else "nas posições"}: ',end='')
for mostra_index,mostra_valor in enumerate(valores):
        if mostra_valor==menor:
            print(f'{mostra_index + 1}, ',end=' ')








