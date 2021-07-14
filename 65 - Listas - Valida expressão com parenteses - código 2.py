    # - DESCREVENDO O DESAFIO
print('65 - Crie um programa onde o usuário digite uma expressão qualquer ',end='')
print('que use parenteses. Seu aplicativo deverá analisar se a expressão está',end=' ')
print('com os parenteses abertos e fechados na ordem correta')
print()

    #INICIALIZANDO O PROGRAMA
    

        # IMPORTA BIBLIOTECAS



            # 1 - RECEBE DADOS

expressão=str(input('digite uma expressão: '))
parenteses=list()

    
            # 2 - MANIPULA E CRIA NOVOS DADOS

for analise in expressão:
    
    if analise=='(':
        parenteses.append(analise)
    elif analise==')':
        if len(parenteses)>0:
            parenteses.pop()
        else:
            parenteses.append(analise)
            break

            
            # 3 - DEVOLVE DAODS

if len(parenteses)==0:
    print(f'\033[32mExpressão válida\033[m')
else:
    print(f'\033[31mExpressão inválida')

