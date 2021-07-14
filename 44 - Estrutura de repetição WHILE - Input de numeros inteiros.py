    # - DESCREVENDO O DESAFIO

print('44 - Crie um programa que leia vários números inteiros pelo teclado.',end='')
print('No final da execução, mostre a média entre todos os valores e qual foi o maior',end='')
print('e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não',end='')
print('continuar a digitar os valores.')
print()


    #INICIALIZANDO O PROGRAMA
    

        # IMPORTA BIBLIOTECAS



            # 1 - RECEBE DADOS, MANIPULA DADOS, CRIA NOVOS DADOS

resp='S'
soma=quant=media=menor=maior=0

while resp in 'Sssim':
        n=int(input('digite um valor: '))
        soma=soma+n
        quant=quant+1
        if quant==1:
            maior=menor=n
        else:
            if n>maior:
                maior=n
            if n<menor:
                menor=n
        resp=str(input('gostaria de continuar?: ')).upper().strip()[0]

media=soma/quant

            
            # 2 - DEVOLVE DAODS

print(f'1 - A média entre os números digitados é {media:.2f} ')
print('2 - O maior valor é {}'.format(maior))
print('3 - O menor valor é {}'.format(menor))
print('4 - Foram digitados {}{}{} números'.format('\033[31m',quant,'\033[m'))







