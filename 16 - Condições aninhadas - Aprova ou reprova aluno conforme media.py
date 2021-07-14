
    # - DESCREVENDO O DESAFIO

print('16 - Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando',end='')

print('uma mensagem no final, de acordo com a média atingida:')
print('1 - Média abaixo de 5.0: REPROVADO')
print('2 - Média entre 5.0 e 6.9: RECUPERAÇAO')
print('3 - Média 7.0 ou superior: APROVADO')

print()



    #INICIALIZANDO O PROGRAMA
    

        # IMPORTA BIBLIOTECAS



            # 1 - RECEBE DADOS

nome = input('Qual seu nome?: ')
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))

    
            # 2 - MANIPULA E CRIA NOVOS DADOS

media = (nota1 + nota2) / 2

            
            # 3 - DEVOLVE DAODS

                      
if media >= 7.0:
    print('1 - Parabéns, {}, você foi \033[1;4;32mAPROVADO\033[m'.format(nome))
    print('2 - Sua média é {}{}{}'.format('\033[1;32m',media,'\033[m'))

elif media <= 4.9:
    print('1 - {}, você foi \033[4;31mREPROVADO\033[m)'.format(nome))
    print('2 - sua média é {}{}{}'.format('\033[31m',media,'\033[m'))

else:
    print('1 - Você está de \033[31mrecuperação\033[m, {}'.format(nome))
    print('2 - sua média é {}{}{}'.format('\033[31m',media,'\033[m'))
