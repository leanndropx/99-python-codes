    # - DESCREVENDO O DESAFIO
print('98 - Reescreva a função leita Int() que fizemos o no desafio 104, incluindo agora a possibilidade ',end='')
print('de digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat()',end='')
print('com a mesma funcionalidade')
print()

    #INICIALIZANDO O PROGRAMA
    

        # IMPORTA BIBLIOTECAS


        # CRIA FUNCOES
        
def leiaInt(msg):
    while True:
        try:
            n=int(input('digite um número inteiro: '))
        except (ValueError,TypeError):
            print('\033[31mERRO, por favor, digite um número inteiro válido\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31m o usuário peferiu não digitar um número inteiro\033[m')
            return 0
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n=float(input('digite um número real: '))
        except (ValueError,TypeError):
            print('\033[31mERRO, digite um número real válido:\033[m ')
            continue
        except KeyboardInterrupt:
            print('\033[31m o usuário preferiu não digitar um número real\033[m')
            return '\033[35m<número não digitado>\033[m'
        else:
            return n

    
            # 2 - USA FUNCOES - RECEBE DADOS, MANIPULA DADOS, RETORNA DADOS

n=leiaInt('digite um número inteiro: ')
r=leiaFloat('digite um número real')
print(f'O valor inteiro digitado foi {n} e o valor Real foi {r} ')







