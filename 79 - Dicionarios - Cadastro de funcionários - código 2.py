    # - DESCREVENDO O DESAFIO
print('79 - Crie um programa que leia nome, ano de nascimento e carteira de trabalho, ',end='')
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
            funcionario['cpts']=int(input('carteira: '))
            if funcionario['cpts']==0:
                if len(todos)!=0:
                    del funcionario['idade']
                    del funcionario['contratacao']
                    del funcionario['salário']
                    del funcionario['aposentadoria']
                todos.append(funcionario.copy())
                p=str(input('mais cadastros?: ')).strip().upper()[0]
                if p=='N':
                    break
            if funcionario['cpts']!=0:
                funcionario['idade']=date.today().year-funcionario['nascimento']
                funcionario['contratacao']=int(input('ano de contratação: '))
                funcionario['salário']=float(input('salario: '))
                funcionario['aposentadoria']=(35-(date.today().year-funcionario['contratacao'])+funcionario['idade'])
                todos.append(funcionario.copy())
                p=str(input('mais cadastros?: ')).strip().upper()[0]
                if p=='N':
                    break

            
            # 2 - RETORNA DADOS


print(f'Foram cadastrados \033[31m{len(todos)}\033[m funcionários.')
for pos,c in enumerate(todos):
            print(f'{"Funcionário":>5} {pos+1}: {"":>4}{c}')

