
    # - DESCREVENDO O DESAFIO

print('45 - Crie um programa que leia vários números inteiros pelo teclado',end='')
print('O programa só vai parar quando o usuário digitar 999, que é a condição de parada. ',end='')
print('No final, mostre quantos números foram digitados e qual foi a soma entre eles',end='')
print('desconsiderando a flag')
print()


    #INICIALIZANDO O PROGRAMA
    

        # IMPORTA BIBLIOTECAS



            # 1 - RECEBE DADOS, MANIPULA DADOS, CRIA NOVOS DADOS

soma=quant=0

while True:
    n=int(input('digite um número: ( \033[7m999 para parar\033[m  ) '))
    if n==999:
        break
    soma=soma+n
    quant=quant+1


            # 3 - DEVOLVE DAODS


print(f'A soma é: {soma}')
print(f'Foram digitados {quant} números')
