
    # - DESCREVENDO O DESAFIO

print('27 - Desenvolva um programa que leia 6 números inteiros e mostre apenas a soma',end='')
print('daqueles que forem pares. Se o valor digitado for impar, desconsidere-os')

print()



    #INICIALIZANDO O PROGRAMA
    

        # IMPORTA BIBLIOTECAS



            # 1 - RECEBE DADOS

                                        # - ESTE PROGRAMA NAO NECESSITA INPUT DE DADOS, ELE OS CRIA
                    
    
            # 2 - MANIPULA DADOS, CRIA DADOS

soma = 0
contagem = 0
for numero in range(1,7):
    
    n = int(input('{} - Digite um número: '.format(numero)))
    
    if n % 2==0:
        soma = soma + n
        contagem = contagem + 1


            
            # 3 - RETORNA DAODS


print('A soma dos {} números pares digitados é: {}'.format(contagem , soma))


