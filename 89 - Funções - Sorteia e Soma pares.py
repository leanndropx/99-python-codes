    # - DESCREVENDO O DESAFIO
print('Desafio 89 - Faça um programa que tenha uma lista chamada números, e duas funções ',end='')
print('chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los ',end='')
print('dentro da lista e a segunda função vai mostrar a soma entre todos os valores PARES ',end='')
print('sorteados pela função anterior')
print()

    #INICIALIZANDO O PROGRAMA
    

        # IMPORTA BIBLIOTECAS

from random import randint

        # CRIA FUNCOES
        
def sorteia():
        
        for c in range(0,5):
            n=randint(0,10)
            numeros_sorteados.append(n)
            numeros.append(n)
        print(f'Os números sorteados foram: {numeros_sorteados}')
        print(f'A lista completa com os numeros que já existiam + numeros sorteados: {numeros}')


def somaPar(numeros):
        soma=0
        for c in numeros:
            if c%2==0:
                soma=soma+c
        print(f'A soma dos números pares sorteados é {soma}')




            # 1 - RECEBE DADOS

numeros_sorteados = []
numeros = [3,2,1,5,4]
    
            # 2 - USA FUNCOES - RECEBE DADOS, MANIPULA DADOS, RETORNA DADOS



sorteia()
somaPar(numeros_sorteados)

