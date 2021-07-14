
    # - DESCREVENDO O DESAFIO

print('43 - Crie um programa que leia vários números inteiros pelo teclado. ',end='')
print('O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.',end='')
print('No final, mostre quantos números foram digitados e qual foi a soma entre eles, ',end='')
print('desconsiderando o flag')
print()


    #INICIALIZANDO O PROGRAMA
    

        # IMPORTA BIBLIOTECAS



            # 1 - RECEBE DADOS

numero=int(input('digite um numero: '))

soma_inputs = 0
conta_inputs = 0
condicao = 999

    
            # 2 - MANIPULA E CRIA NOVOS DADOS

while numero != condicao:
    
    conta_inputs = conta_inputs + 1
    soma_inputs = soma_inputs + numero
    numero = int(input('digite um numero: '))

            
            # 3 - DEVOLVE DAODS

print('1 - quantidade de números digitados: {}{}{}'.format('\033[35m',conta_inputs,'\033[m'))
print('2 - soma dos números digitados: {}{}{}'.format('\033[35m',soma_inputs,'\033[m'))








