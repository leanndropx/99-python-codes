
    # - DESCREVENDO O DESAFIO

print('34 - Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas',end='')
print('e no final do programa mostre:')
print('1 - a idade da pessoa mais velha')
print('2 - a média de idade do grupo')
print('3 - qual é o nome do homem mais velho')
print('4 - quantas mulheres tem menos de 20 anos')
print()



    # - INICIALIZANDO O PROGRAMA
    

        # IMPORTA BIBLIOTECAS



            # 1 - RECEBE DADOS

nome_homem_mais_velho=''
soma_idade = 0
media_idade = 0

idade_pessoa_mais_velha = 0

conta_mulheres_abaixo_20 = 0


for contador in range(1,5):

    nome=str(input('Nome?: ')).strip()
    idade=int(input('Idade: '))
    sexo=str(input('sexo [M/F]: ')).strip().lower()
    
    print()

            # 2 - MANIPULA E CRIA NOVOS DADOS

    soma_idade+=idade
    media_idade = soma_idade / contador


    if contador == 1:
        idade_pessoa_mais_velha = idade
        if sexo=='m':
            idade_homem_mais_velho = idade
            nome_homem_mais_velho = nome
    else:
        
        if idade > idade_pessoa_mais_velha:
            idade_pessoa_mais_velha = idade
        
        if sexo == 'm':
            
            if idade > idade_homem_mais_velho:
                idade_homem_mais_velho = idade
                nome_homem_mais_velho = nome

    if idade < 20 and sexo == 'f':
        conta_mulheres_abaixo_20 = conta_mulheres_abaixo_20 + 1



            # 3 - DEVOLVE DAODS


print('1 - A idade da pessoa mais velha é {}'.format(idade_pessoa_mais_velha))

print('2 - A media de idade é {}'.format(media_idade))

print('3 - {} {} tem menos de 20 anos'.format(conta_mulheres_abaixo_20,'mulher' if conta_mulheres_abaixo_20 == 1 else 'mulheres'))

print('4 - O nome do homem mais velho é {}, com idade de {} anos '.format(nome_homem_mais_velho, idade_homem_mais_velho))
