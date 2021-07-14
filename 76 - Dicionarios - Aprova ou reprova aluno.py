    # - DESCREVENDO O DESAFIO
print('76 - Faça um programa que leia nome e média de um aluno ',end='')
print('guardando também a situação em um dicionario')
print('No final, mostre o conteúdo da estrutura na tela')
print()

    #INICIALIZANDO O PROGRAMA
    

        # IMPORTA BIBLIOTECAS



            # 1 - RECEBE DADOS

aluno={}
aluno['nome']=str(input('nome: '))
aluno['media']=float(input(f'média do {aluno["nome"]}: '))


            # 2 - MANIPULA E CRIA NOVOS DADOS

if aluno['media']<5:
        aluno['situacao']='\033[31mREPROVADO'
else:
        aluno['situacao']='\033[32mAPROVADO'

            
            # 3 - DEVOLVE DAODS

for key,value in aluno.items():
        print(f'{key} é igual a {value}')
