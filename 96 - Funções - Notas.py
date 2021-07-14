    # - DESCREVENDO O DESAFIO
print('Deafio 96 - Faça um programa que tenha uma função chamada notas() que pode receber várias notas de alunos.')
print('Ele vai retornar um dicionario com as seguintes informações:')
print('1 - quantidade de notas')
print('2 - a maior nota')
print('3 - a menor nota')
print('4 - a média da turma')
print('5 - a situação (opcional)')
print('Adicione também as docstrings da função')
print()

    #INICIALIZANDO O PROGRAMA


        # CRIA FUNCOES
        
def notas(*valores,sit=False):
        """-----------------------------------------
        Calcula e mostra informações de notas dos alunos
        :param *valores: usuário informa a quantidade de notas que desejar, sempre através de vírgula
        :param sit=True: opcional, se usuario informar sit=True programa mostra se a situação do aluno é BOA, RUIM OU RAZOAVEL
        :param sit=False: opcional, se usuário informar sit=False programa não mostra situação do aluno
        :return: retorna para as informações contidas na lista"""

        notas={}
        soma=maior=menor=0
        for index,valor in enumerate(valores):
            if index==0:
                maior=menor=valor
            else:
                if valor>maior:
                    maior=valor
                if valor<menor:
                    menor=valor
            soma=soma+valor
        notas['Quantidade de notas']=len(valores)
        notas["media"]=soma/len(valores)
        notas['maior']=maior
        notas['menor']=menor
        if sit==True:
            if notas['media']>=5 and notas['media']<=7:
                notas['situação']='RAZOAVEL'
            elif notas['media']<5:
                notas['situação']='RUIM'
            else:
                notas['situação']='BOA'

            return (notas)
        else:
            return (notas)

                        
            # 2 - USA FUNCOES - RECEBE DADOS, MANIPULA DADOS, RETORNA DADOS

print(notas(1,3,9,7,8,0))
notas(10,9,8)
notas(5,7)
print(notas(4,7,8,2,6,0,0,0,0,sit=True))
help(notas)







