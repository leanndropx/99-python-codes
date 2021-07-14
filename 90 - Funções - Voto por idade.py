    # - DESCREVENDO O DESAFIO
print('Desafio 90 - Crie um programa que tenha uma função chamada voto() que vai receber ',end='')
print('como parametro o ano de nascimento de uma pessoa, retornado um valor literal indicando',end=' ')
print('se uma pessoa tem voto negado, opcional ou obrigatorio nas eleições')
print()

    #INICIALIZANDO O PROGRAMA
    

        # IMPORTA BIBLIOTECAS


        # CRIA FUNCOES
        
def voto(ano_de_nascimento):
        from datetime import date
        
        idade=date.today().year - ano_de_nascimento

        if idade>=16 and idade<18 or idade>75:
            return f'Com {idade} anos: voto opcional'
        elif idade>18:
            return f'Com {idade} anos: voto obrigatório'
        else:
            return f'Com {idade} anos: ainda não pode votar'

                        
            # 1 - RECEBE DADOS

ano=int(input('em que ano você nasceu?:  '))
    
            # 2 - USA FUNCOES - RECEBE DADOS, MANIPULA DADOS, RETORNA DADOS

print(voto(ano))










