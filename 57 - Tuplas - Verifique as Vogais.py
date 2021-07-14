    # - DESCREVENDO O DESAFIO
print('57 - Crie um programa que tenha uma tupla com várias palavras',end='')
print('(não usar acentos). Depois disso, deve mostrar, pra cada palavra',end='')
print('quais são suas vogais')
print()


    #INICIALIZANDO O PROGRAMA
    

        # IMPORTA BIBLIOTECAS



            # 1 - RECEBE DADOS

palavras=('Camiseta',
          'Elefante',
          'Urina',
          'Igreja',
          'gratis',
          'paralelepipedo',
          'inconstitucionalicimamente')

    
            # 2 - MANIPULA DADOS, RETORNA DADOS CONFORME CONDICAO

for palavra in palavras:
        print(f'\nNa palavra {palavra} existem as vogais: ',end='')
        for vogal in palavra:
            if vogal.lower() in 'aeiou':
                print(vogal,end=' ')








