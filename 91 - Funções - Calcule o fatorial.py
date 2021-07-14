    #DESCREVENDO O DESAFIO
print('Desafio 91 - Crie um programa que tenha uma função fatorial() que receba dois parâmetros, ',end='')
print('o primeiro que indique o numero a calcular e o outro chamado show, que será um valor lógico opcional ',end='')
print('indicando se será mostrado ou não na tela o processo de cálculo fatorial.')
print()

    #INICIALIZANDO O PROGRAMA
    

        # IMPORTA BIBLIOTECAS


        # CRIA FUNCOES
        
def fatorial(n,show=False):
    """
    ------------------------------------------------
    ->Calcula o fatorial de um número.
    :param n: O número a ser calculado
    :param show: (opcional), mostrar ou não a conta
    return: O valor do Fatorial de um número n

    """

    f=1
    for c in range(n,0,-1):
        if show:
            print(c,end='')
            if c>1:
                print(" x ",end='')
            else:
                print(f'{" = "}',end='')
        f = f * c
    return f

                        
            # 1 - RECEBE DADOS

n=int(input('gostaria de ver o fatorial de qual numero?: '))
    
            # 2 - USA FUNCOES - RECEBE DADOS, MANIPULA DADOS, RETORNA DADOS

print(fatorial(n,show=True))
help(fatorial)









