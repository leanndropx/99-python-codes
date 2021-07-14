    # - DESCREVENDO O DESAFIO
print('49 - Crie um programa que leia o nome e o preço de vários produtos. ',end='')
print('O programa deverá perguntar se o usuário vai continuar. No final, mostre: ')
print('1 - qual é o total gasto na compra.')
print('2 - quantos produtos custam mais de R$1.000')
print('3 - qual é o nome do produto mais barato')
print(' ')



    #INICIALIZANDO O PROGRAMA
    

        # IMPORTA BIBLIOTECAS



            # 1 - RECEBE DADOS

total=0
totmil=0
quant=0
menor=0
produto_mais_barato=''

while True:
        produto=str(input('Nome do produto: '))
        preço=float(input('Preço: R$ '))
        total=total+preço
        quant=quant+1

                # 2 - MANIPULA E CRIA NOVOS DADOS

        if preço>1000:
            totmil=totmil+1
        if quant==1 or preço<menor:
            menor=preço
            produto_mais_barato = produto

        resp=' '
        while resp not in 'SN':
            resp=str(input('Deseja continuar?: ')).strip().upper()[0]
        if resp=='N':
            break
        print(' ')


            
            # 3 - DEVOLVE DAODS

print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total gasto na compra foi R${total:^20.2f}.')
print(f'{totmil:^10} produtos custam mais de mil reais')
print(f'O nome do produto mais barato é {produto_mais_barato.upper():^20}')






