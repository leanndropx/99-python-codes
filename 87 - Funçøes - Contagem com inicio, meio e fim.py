    # - DESCREVENDO O DESAFIO
print('87 - Faça uma função chamada contador(), que receba 3 parâmetros: início, fim e passo ',end='')
print('e realize a contagem. Seu programa tem que realizar 3 contagens através da função criada: ')
print('1 - De 1 até 10, contando de 1 em 1')
print('2 - De 10 até 0, contando de 2 em 2')
print('3 - Uma contagem personalizada')
print()

    #INICIALIZANDO O PROGRAMA
    

        # IMPORTA BIBLIOTECAS

from time import sleep

        # CRIA FUNCOES
        
def contador(inicio, fim, passo):
        print(f'Contagem de {inicio} a {fim} de {passo} em {passo}')
        print('*'*50)
        if passo < 0:
            passo = passo *(-1)
        
        if passo == 0:
            passo = 1
        
        if inicio < fim:
            cont=inicio
            while cont <= fim:
                print(f'{cont}  ',end='',flush=True)
                sleep(0.3)
                cont=cont+passo
            print()
            print('*'*50)
        else:
            cont=inicio
            while cont >= fim:
                print(f'{cont}  ',end='',flush=True)
                sleep(0.3)
                cont=cont-passo
            print()
            print('*'*50)
        print()

                        
            # 1 - RECEBE DADOS

inicio = int(input('inicio: '))
fim = int(input('fim: '))
passo = int(input('passo: '))

    
            # 2 - USA FUNCOES - RECEBE DADOS, MANIPULA DADOS, RETORNA DADOS

contador(0,10,1)
contador(100,0,10)
contador(inicio,fim,passo)









