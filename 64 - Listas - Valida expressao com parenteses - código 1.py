    # - DESCREVENDO O DESAFIO
print('64 - Crie um programa onde o usuário digite uma expressão qualquer ',end='')
print('que use parenteses. Seu aplicativo deverá analisar se a expressão está',end=' ')
print('com os parenteses abertos e fechados na ordem correta')
print()


    #INICIALIZANDO O PROGRAMA
    

        # IMPORTA BIBLIOTECAS



            # 1 - RECEBE DADOS

expressao=str(input('digite a expressao: '))

contador_abre_parenteses=0
contador_fecha_parenteses=0

            # 2 - MANIPULA DADOS, RETORNA DADOS

for caractere in expressao:
    
        if caractere == '(':
            contador_abre_parenteses = contador_abre_parenteses + 1
        
        elif caractere == ')':
            contador_fecha_parenteses = contador_fecha_parenteses + 1


if contador_abre_parenteses == contador_fecha_parenteses:
        
        print('A expressão é CORRETA')

    else:
        print('A expressão é INCORRETA')

            







