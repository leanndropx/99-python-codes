
    # - DESCREVENDO O DESAFIO

print('46 - Faça um programa que mostre a tabuada de vários números,',end='')
print('um de cada vez, para cada valor digitado pelo usuário.',end='')
print('O programa será interrompido quando o número solicitado for negativo.')
print()


    #INICIALIZANDO O PROGRAMA
    

        # IMPORTA BIBLIOTECAS



            # 1 - RECEBE DADOS

while True:
    numero = int(input('quer ver a tabuada de qual valor?: '))

            # 2 - MANIPULA, CRIA NOVOS DADOS, DEVOLVE DADOS

    if numero < 0:
        break
    print('-'*30)
    
    for contagem in range(1,11):
        print(f'{numero} x {contagem} = {numero * contagem}')
    print('-'*30)


print('ACABOU')


            





    
