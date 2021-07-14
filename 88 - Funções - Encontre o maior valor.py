    # - DESCREVENDO O DESAFIO
print('Desafio 88 - Faça um programa que tenha uma função chamada maior(), que receba varios',end='')
print('varios parametros com valores inteiros. Seu programa tem que analisar todos os valores ',end='')
print('e dizer qual deles é o maior')
print()

    #INICIALIZANDO O PROGRAMA
    

        # IMPORTA BIBLIOTECAS


        # CRIA FUNCOES
        
def maior(*valores):
    maior=0
    print('VAMOS ANALISAR: ')
    print('*' * 20)
    print('Os números informados foram: ',end='')

    for c in valores:
        print(F'{c} > ',end='',flush=True)
        if c==0:
            maior=c
        else:
            if c>maior:
                maior=c
        sleep(0.3)
    print('FIM')
    print(f'1 - Foram informados {len(valores)} valores')
    sleep(0.3)
    print(f'2 - O maior valor é {maior} ')
    print('*'*20)
    print()
    sleep(1)


    
            # 1 - USA FUNCOES - RECEBE DADOS, MANIPULA DADOS, RETORNA DADOS

maior(1,2,5,3)
maior(10,6,54,1,98,43)









