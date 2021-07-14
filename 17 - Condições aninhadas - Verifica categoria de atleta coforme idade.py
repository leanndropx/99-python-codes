
    # - DESCREVENDO O DESAFIO

print('17 - A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento',end='')
print('de um atleta e mostre sua categoria, de acordo com a idade:')

print('1 - Até 9 anos: MIRIM')
print('2 - Até 14 anos: INFANTIL')
print('3 - Até 19 anos: JUNIOR')
print('4 - Até 20 anos: SENIOR')
print('5 - Acima de 20 anos: MASTER')



    #INICIALIZANDO O PROGRAMA

import datetime

        # IMPORTA BIBLIOTECAS



            # 1 - RECEBE DADOS

sexo = input('Sexo do altleta - Digite 1 para masculino ou 2 para feminino: ').strip()

if sexo=='1':
        print('O sexo especificado foi MASCULINO')
        sexo='masculino'

elif sexo=='2':
        print('O sexo especificado foi FEMININO')
        sexo='feminino'
 
elif sexo!=1 and sexo!=2:
        erro=input('Sexo não especificado corretamente. Gostaria de responder novamente?: ').upper()
        if erro == 'SIM':
            print('OK, mas primeiro vamos continuar')


print()
nome = input('Nome do atleta: ')
ano_de_nascimento = int(input('Digite seu ano de nascimento: '))



    
            # 2 - MANIPULA E CRIA NOVOS DADOS

ano_atual = datetime.date.today().year

idade = ano_atual - ano_de_nascimento


            
            # 3 - DEVOLVE DAODS


if idade <= 9:
    print('1 - Categoria d{} atleta {}: MIRIM'.format('a' if sexo=='feminino' else 'o',nome.upper()))

elif idade >=10 and idade <= 14:
    print('1 - Categoria d{} atleta {}: INFANTIL'.format('a' if sexo=='feminino' else 'o',nome.upper()))

elif idade >= 15 and idade <= 19:
    print('1 - Categoria d{} atleta {}: JUNIOR'.format('a' if sexo=='feminino' else 'o',nome.upper()))

elif idade == 20:
    print('Categoria d{} atleta {}: SENIOR'.format('a' if sexo=='feminino' else 'o',nome.upper()))

else:
    print('Categoria d{} atleta {}: MASTER'.format('a' if sexo=='feminino' else 'o',nome.upper()))




