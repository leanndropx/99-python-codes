    # - DESCREVENDO O DESAFIO
print('78 - Crie um programa que leia nome, ano de nascimento e carteira de trabalho, ',end='')
print('e cadastre-os (com idade) em um dicionario se por acaso a CPTS for diferente de zero.')
print('O dicionario também receberá o ano de contratação e o salário.')
print('Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.')
print()

    #INICIALIZANDO O PROGRAMA
    

        # IMPORTA BIBLIOTECAS

from _datetime import date


            # 1 - RECEBE DADOS

funcionario={}
todos_funcionarios=[]

while True:
        funcionario['nome']=str(input('nome: '))
        funcionario['nascimento']=int(input('ano de nascimento: '))
        funcionario['cpts']=int(input('carteira: '))
        if funcionario['cpts']==0:
            if len(todos)!=0:
                del funcionario['idade']
                del funcionario['contratacao']
                del funcionario['salário']
                del funcionario['aposentadoria']
            
            todos_funcionarios.append(funcionario.copy())
            
            p=str(input('mais cadastros?: ')).strip().upper()[0]
            if p=='N':
                break
        if funcionario['cpts']!=0:
            funcionario['idade']=date.today().year-funcionario['nascimento']
            funcionario['contratacao']=int(input('ano de contratação: '))
            funcionario['salário']=float(input('salario: '))
            funcionario['aposentadoria']=(35-(date.today().year-funcionario['contratacao'])+funcionario['idade'])
            
            todos_funcionarios.append(funcionario.copy())
            p=str(input('mais cadastros?: ')).strip().upper()[0]
            if p=='N':
                break


    
            # 2 - MANIPULA DADOS, RETORNA DADOS CONFORME CONDICAO

print(f'\033[7m{"Nome":^20}{"Ano de nascimento":^20}{"CPTS":^20}{"Idade":^20}{"Ano de contratação":^20}{"Salário":^20}{"Aposentadoria":^20}\033[m')
for pos,c in enumerate(todos_funcionarios):
        for k,v in c.items():
            print(f'{v:^20}',end='')
        print()

            







