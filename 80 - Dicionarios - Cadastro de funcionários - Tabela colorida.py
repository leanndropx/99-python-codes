    # - DESCREVENDO O DESAFIO
print('80 - Crie um programa que leia nome, ano de nascimento e carteira de trabalho, ',end='')
print('e cadastre-os (com idade) em um dicionario se por acaso a CPTS for diferente de zero.')
print('O dicionario também receberá o ano de contratação e o salário.')
print('Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.')
print()

    #INICIALIZANDO O PROGRAMA
    

        # IMPORTA BIBLIOTECAS

from _datetime import date

            # 1 - RECEBE DADOS, MANIPULA DADOS

funcionario={}
todos=[]

while True:
    funcionario['nome']=str(input('nome: '))
    funcionario['nascimento']=int(input('ano de nascimento: '))
    funcionario['orientacao']=str(input('orientação sexual: ')).strip().lower()
    funcionario['cpts']=int(input('carteira: '))

    if funcionario['cpts']!=0:
        funcionario['idade']=date.today().year-funcionario['nascimento']
        funcionario['contratacao']=int(input('ano de contratação: '))
        funcionario['salário']=float(input('salario: '))
        funcionario['aposentadoria']=(35-(date.today().year-funcionario['contratacao'])+funcionario['idade'])
        todos.append(funcionario.copy())
        p=str(input('mais cadastros?: ')).strip().upper()[0]
        if p=='N':
            break
    if funcionario['cpts']==0:
        funcionario['idade']='-'
        funcionario['contratacao']='-'
        funcionario['salario']='-'
        funcionario['aposentadoria']='-'
        todos.append(funcionario.copy())
        p=str(input('mais cadastros?: ')).strip().upper()[0]
        if p=='N':
            break


            # 3 - RETORNA DAODS

import random
escolha='.'

print(f'\033[7m{"Nome":^20}{"Ano de nascimento":^20}{"Orientação sexual":^20}{"CPTS":^20}{"Idade":^20}{"Ano de contratação":^20}{"Salário":^20}{"Aposentadoria":^20}\033[m')
for pos,c in enumerate(todos):
    for k,v in c.items():
        if v==c['orientacao'] and c['orientacao'] in 'gaybissexualtransexuallesbicasapatao':
            cores=['\033[7;31m','\033[7;32m','\033[7;33m','\033[7;35m','\033[7;34m']

            if pos==0:
                print('\033[7;35m',end='')
            else:
                escolha='\033[7;35m'
                escolhida=['\033[7;35m']

                if len(escolhida)==1:
                    while escolha==escolhida[-1]:
                        escolha=random.choice(cores)
                    escolhida.append(escolha)
                    print(escolhida[-1], end='')

                elif len(escolhida)>1:
                    while escolha == escolhida[-1]:
                        while escolha==escolhida[-2]:
                            escolha = random.choice(cores)
                    escolhida.append(escolha)
                    print(escolhida[-1], end='')

        print(f'{v:^20}',end='')
        print('\033[m',end='')
    print()








