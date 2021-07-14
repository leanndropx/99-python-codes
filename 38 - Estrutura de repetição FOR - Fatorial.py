
    # - DESCREVENDO O DESAFIO

print('38 - Faça um programa que leia um número qualquer e mostre o seu fatorial')
print()


    #INICIALIZANDO O PROGRAMA
    

        # IMPORTA BIBLIOTECAS



            # 1 - RECEBE DADOS

numero = int(input('digite um número: '))

fatorial=1
    
            # 2 - MANIPULA E CRIA NOVOS DADOS

for c in range(numero,0,-1):
    print(c,end='  ')
    print(' x ' if c>1 else ' = ',end=' ')
    fatorial=fatorial*c


            # 3 - DEVOLVE DAODS

print('\033[35m',fatorial)









