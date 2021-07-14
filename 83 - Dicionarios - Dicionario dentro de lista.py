    # - DESCREVENDO O DESAFIO
print('83 - Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados ',end='')
print('de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: ')
print('1 - quantas pessoas foram cadastradas')
print('2 - a média de idade do grupo')
print('3 - uma lista com todas as mulheres')
print('4 - uma lista com todas as pessoas com idade acima da média')
print()

    #INICIALIZANDO O PROGRAMA
    

        # IMPORTA BIBLIOTECAS

import math

            # 1 - RECEBE DADOS

pessoas=[]
dados={}
soma_idade=total_pessoas=0
mulheres=[]
acima_media=[]

while True:
        dados['nome']=str(input('nome: ')).strip().capitalize()
        dados['sexo']=str(input('sexo: ')).strip().upper()
        dados['idade']=int(input('idade: '))
        pessoas.append(dados.copy())
        total_pessoas=total_pessoas+1
        soma_idade=soma_idade+dados['idade']
        if dados['sexo']=='F':
            mulheres.append(dados.copy())

        p=str(input('mais?: ')).strip().upper()[0]
        if p in 'N':
            break


    
            # 2 - MANIPULA DADOS

media=soma_idade/total_pessoas

            
            # 3 - DEVOLVE DAODS

for pessoa in pessoas:
        for key,value in pessoa.items():
            if value == pessoa['idade'] and pessoa['idade']>media:
                acima_media.append(pessoa)

print(pessoas)
print(mulheres)
print(acima_media)

print(' ')
print(f'{"":>10}Foram cadastradas {total_pessoas} pessoas')
print(f'{"":>10}A média de idade do grupo é de {math.ceil(media)} anos')

if len(mulheres)==0:
        print(f'{"":>10}Não houve cadastro de mulheres',end='')
else:
        print(f'{"":>10}As mulheres cadastradas são: ',end='')
        for mulher in mulheres:
            print(f'{mulher["nome"]}, ',end=' ')

print()
print(f'{"":>10}As pessoas com idade acima da média são: ',end='')
for pessoa in acima_media:
        print(f'{pessoa["nome"]}, ',end='')










