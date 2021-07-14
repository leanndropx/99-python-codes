
    # - DESCREVENDO O DESAFIO

print('31 - Crie um programa que leia uma frase qualquer e diga se ela é palíndromo',end='')
print('desconsiderando os espaços')

print()



    #INICIALIZANDO O PROGRAMA
    

        # IMPORTA BIBLIOTECAS



            # 1 - RECEBE DADOS

frase=str(input('Digite uma frase: ')).strip().lower()

    
            
            # 2 - MANIPULA DADOS, RETORNA DADOS COM CONDICAO

frase_dividida = frase.split()
frase_sem_espaco = ''.join(frase_dividida)
frase_invertida_sem_espaco =''



for letra in range (len(frase_sem_espaco)-1,-1,-1):
    
    frase_invertida_sem_espaco += frase_sem_espaco [letra]

if frase_sem_espaco == frase_invertida_sem_espaco:
    print('1 - A frase é um Palíndromo')
    print('2 - {} = {}'.format(frase_sem_espaco, frase_invertida_sem_espaco))

else:
    print('1 - A frase não é um palíndromo')
    print('2 - {} = {}'.format(frase_sem_espaco, frase_invertida_sem_espaco))






