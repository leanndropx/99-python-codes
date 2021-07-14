
    # - DESCREVENDO O DESAFIO

print('15 - Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade: ')
print('1 - Se ele ainda vai se alistar no serviço militar')
print('2 - Se é a hora de se alistar')
print('3 - Se já passou do tempo de alistamento')
print('Seu programa também deve mostrar o tempo que falta ou se passou do prazo')
print()



    #INICIALIZANDO O PROGRAMA
    
from datetime import date

        # IMPORTA BIBLIOTECAS


            # 1 - RECEBE DADOS

nome = input('Qual seu nome?: ')
ano_de_nascimento = int(input('Em que ano você nasceu?: '))
ano_atual = date.today().year

    
            # 2 - MANIPULA E CRIA NOVOS DADOS

idade = ano_atual - ano_de_nascimento

quantos_anos_faltam_pra_18 = ano_atual - (ano_de_nascimento + 18)


            # 3 - DEVOLVE DAODS


if idade > 18:
    
        print('1 - Já passou da hora de se alistar, {} !'.format(nome))
    
        print('2 - Você deveria ter se alistado há {} {} atrás.'.format(quantos_anos_faltam_pra_18,'ano' if quantos_anos_faltam_pra_18==1 else 'anos'))


elif idade == 18:
    
        print('Este ano você precisa se alistar, {}!'.format(nome))


elif idade < 18:
    
        print('Faltam {} {} para você se alistar, {} !'.format( quantos_anos_faltam_pra_18 *(-1),'ano' if quantos_anos_faltam_pra_18 == (-1 or 1) else 'anos', nome))

