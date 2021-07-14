
    # - DESCREVENDO O DESAFIO

print('28 - Desenvolva um programa que leia o primeiro termo e a razão de uma PA',end='')
print('No final, mostre os 10 primeiros termos dessa progressão')

print()



    #INICIALIZANDO O PROGRAMA
    

        # IMPORTA BIBLIOTECAS



            # 1 - RECEBE DADOS

primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))


            # 2 - MANIPULA DADOS

ultimo_termo = primeiro_termo + (razao*10)

            # 3 - RETORNA DADOS

print('Os 10 primeiros termos desta progressão são: ')

for termo in range (primeiro_termo, ultimo_termo , razao):
    
    print (termo, end=' > ')

print('ACABOU')





