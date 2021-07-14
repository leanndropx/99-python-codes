
    # - DESCREVENDO O DESAFIO

print('32 - Crie um programa que leia o ano de nascimento de 7 pessoas',end='')
print('No final, mostre quantas pessoas ainda não atingiram a maioridade',end='')
print('e quantas já são maiores')
print()


    #INICIALIZANDO O PROGRAMA
    

        # IMPORTA BIBLIOTECAS

import datetime

            # 1 - RECEBE DADOS

ano_atual = datetime.date.today().year
conta_maior_de_idade = 0

for c in range(1,8):
    ano_de_nascimento = int(input('{} - Digite o ano de nascimento: '.format(c)))
    
    if (ano_atual - ano_de_nascimento) >= 18:
        
        print('Você é maior de idade e sua idade é {}.'.format(ano_atual - ano_de_nascimento))
        conta_maior_de_idade = conta_maior_de_idade + 1

print()

    
            # 2 - MANIPULA DADOS, RETORNA DADOS

if conta_maior_de_idade == 7:
    print('Todas as pessoas são maiores de idade')

elif conta_maior_de_idade < 7 and conta_maior_de_idade != 0:
    
    print(f'1 - {conta_maior_de_idade} pessoas são maiores de idade.')
    print(f'2 - {7 - conta_maior_de_idade} ainda são menores de idade.')

else:
    print('Ninguém é maior de idade')
