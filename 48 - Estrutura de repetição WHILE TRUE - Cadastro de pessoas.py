    # - DESCREVENDO O DESAFIO
print('48 - Crie um programa que leia a idade e o sexo de várias pessoas. ',end='')
print('A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. ',end='')
print('No final, mostre:')
print('1 - quantas pessoas tem mais de 18 anos.')
print('2 - quantos homens foram cadastrados')
print('3 - quantas mulheres tem menos de 20 anos')
print(' ')



    #INICIALIZANDO O PROGRAMA
    

        # IMPORTA BIBLIOTECAS



            # 1 - RECEBE DADOS

quant=0
maior_dezoito=0
homens_mais_dezoito=0
quant_homens=0
mulheres_menos_vinte=0

while True:
        print('\033[7m  CADASTRE UMA PESSOA  \033[m')

        idade=int(input('digite sua idade: '))
        sexo=str(input('digite seu sexo [M/F]: ')).strip().upper()[0]

        while sexo!='M' and sexo!='F':
            sexo=str(input('digite seu sexo [M/F]: ')).strip().upper()[0]
        pergunta=str(input('deseja continuar?: ')).strip().upper()[0]
        print()
        quant=quant+1

        
            # 2 - MANIPULA E CRIA NOVOS DADOS

        if idade>=18:
            maior_dezoito=maior_dezoito+1
        if sexo in 'M':
            quant_homens=quant_homens+1
        if sexo in 'F' and idade<20:
            mulheres_menos_vinte=mulheres_menos_vinte+1
        if pergunta in 'N':
            break


            
            # 3 - DEVOLVE DAODS

print('1 - pessoas com mais de 18 anos: {}{}{}'.format('\033[31m',maior_dezoito,'\033[m'))
print('2 - quantidade de homens cadastrados: {}{}{}'.format('\033[31m',quant_homens,'\033[m'))
print('3 - mulheres com menos de 20 anos: {}{}{}'.format('\033[31m',mulheres_menos_vinte,'\033[m'))
print('4 - total de pessoas cadastradas: {}{}{}'.format('\033[35m',quant,'\033[m'))







