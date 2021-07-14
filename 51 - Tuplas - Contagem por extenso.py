    # - DESCREVENDO O DESAFIO
print('51 - Crie um programa que tenha uma tupla totalmente preenchida ',end='')
print('com uma contagem por extenso, de zero até vinte.')
print('Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostra-lo por extenso')
print()



    #INICIALIZANDO O PROGRAMA
    

        # IMPORTA BIBLIOTECAS



            # 1 - RECEBE DADOS

escreve = ('zero','um','dois','tres','quatro','cinco',
      'seis','sete','oito','nove','dez',
      'onze','doze','treze','catorze','quinze',
      'dezesseis','dezessete','dezoito','dezenove','vinte')


    
            # 2 - MANIPULA E CRIA NOVOS DADOS

while True:
        numero = int(input('digite um número entre 0 e 20: '))
        if numero >0 or numero <20:
            break


            # 3 - DEVOLVE DAODS

print('O número digitado foai {}'.format(escreve[numero]))







