
    # - DESCREVENDO O DESAFIO

print('25 - Faça um programa que calcule a soma entre todos os números impares',end='')
print('que são múltiplos de 3 e que se encontram no intervalo de 1 até 500')

print()

    #INICIALIZANDO O PROGRAMA
    

        # IMPORTA BIBLIOTECAS



            # 1 - RECEBE DADOS

                                                # - ESTE PROGRAMA NAO NECESSITA INPUT DE DADOS, ELE OS CRIA
    
    
    
            # 2 - MANIPULA E CRIA NOVOS DADOS


soma = 0
contagem = 0


for impar in range(0+1,501,2):
    
    if impar % 3 == 0:
        soma = soma + impar
        contagem = contagem + 1


            # 3 - DEVOLVE DAODS

print(' 1 - A soma entre os números impares que são múltiplos de 3 é: {}'.format(soma))
print(' 2 - A quantidade de números impares múltiplos de 3 é: {}'.format(contagem))
print(' 2 - Os números impares múltiplos de 3 são:')
for impar in range(0+1,501,2):
    if impar %3 == 0:
        print(impar,end='  ')










