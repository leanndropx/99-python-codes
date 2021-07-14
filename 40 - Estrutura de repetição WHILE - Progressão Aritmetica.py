
    # - DESCREVENDO O DESAFIO

print('40 - Refaça o desafio 51, lendo o primeiro termo e a razão de uma PA',end='')
print('mostrando os 10 primeiros termos da progressão usando a estrutura WHILE')
print()


    #INICIALIZANDO O PROGRAMA
    

        # IMPORTA BIBLIOTECAS



            # 1 - RECEBE DADOS

primeiro_termo = int(input('digite o primeiro termo: '))
razao = int(input('digite a razão: '))

    
            # 2 - MANIPULA DADOS, RETORNA DADOS CONFORME CONDICAO

proximo_termo = primeiro_termo
contador=1

while contador<=10:
    print('{} < '.format(proximo_termo),end=' ')
    proximo_termo = proximo_termo + razao
    contador=contador+1

print('FIM')










