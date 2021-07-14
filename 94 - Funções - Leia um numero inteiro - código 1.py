    # - DESCREVENDO O DESAFIO
print('Desafio 94 - Crie um programa que tenha a função leiaInt(), que vai funcionar de forma',end='')
print('semelhante a função Input() do Python, só que fazendo a validação para aceitar apenas 1 valor numérico')
print('Ex: leitaInt("Digite um numero"')
print()

    #INICIALIZANDO O PROGRAMA


        # IMPORTA BIBLIOTECAS
        
        
        # CRIA FUNCOES
        
def inputInt(msg):
    msg=str(input(msg))
    if msg.isnumeric():
        msg=int(msg)
    elif msg.count('.')==1:
        msg=float(msg)
    else:
        while True:
            msg=str(input('\033[31mERRO, digite um valor numérico:\033[m '))
            if msg.count('.')==1:
                msg=float(msg)
                break
            elif msg.isnumeric():
                msg=int(msg)
                break
    return msg

                        
            # 1 - RECEBE DADOS

n=inputInt('Digite um numero: ')
    
            # 2 - USA FUNCOES - RECEBE DADOS, MANIPULA DADOS, RETORNA DADOS

print(f'O valor digitado foi {n}')
print(type(n))



