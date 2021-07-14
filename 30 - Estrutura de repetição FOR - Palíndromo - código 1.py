
    # - DESCREVENDO O DESAFIO

print('30 - Cria um programa que leia uma frase qualquer e diga se ela é um palíndromo',end='')
print('desconsiderando os espaços')

print()



    #INICIALIZANDO O PROGRAMA
    

        # IMPORTA BIBLIOTECAS



            # 1 - RECEBE DADOS

frase=input('Digite uma frase: ')

    
            # 2 - MANIPULA DADOS

frase_sem_espaco = frase.strip().lower().replace(' ','')

            
            # 3 - RETORNA DAODS CONFORME CONDICAO


if frase_sem_espaco [0:] == frase_sem_espaco [::-1]:
    
    print('1 - Verdade')
    
    print('2 - A frase "{}{}{}" é um palíndromo porque: '.format('\033[35m',frase.capitalize(),'\033[m'))
    
    print('3 - "{}" = "{}"'.format( frase[::].upper(), frase[::-1].upper() ))

else:
    print('1 - Mentira')
    
    print('2 - A frase "{}{}{}" não é um palíndromo porque:'.format('\033[35m',frase.capitalize(),'\033[m'))
    
    print('3 - "{}{}{}" é diferente de "{}{}{}"'.format('\033[35m',frase.upper(),'\033[m','\033[35m',frase[::-1].upper(),'\033[m'))







