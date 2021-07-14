    # - DESCREVENDO O DESAFIO
print('Desafio 95 - Crie um programa que tenha a função leiaInt(), que vai funcionar de forma',end='')
print('semelhante a função Input() do Python, só que fazendo a validação para aceitar apenas 1 valor numérico')
print('Ex: leitaInt("Digite um numero"')
print()

    #INICIALIZANDO O PROGRAMA


        # IMPORTA BIBLIOTECAS
        
        
        # CRIA FUNCOES
        
def input_1(msg):
    ok=False
    while True:
        n = str(input(msg))
        if n.isnumeric():
            n=int(n)
            ok=True
        elif n.count('.')==1:
            n=float(n)
            ok=True
        if ok:
            break
        print('\033[31mERRO, o valor precisa ser numérico\033[m ')
    return n

                        
            # 1 - RECEBE DADOS

n=input_1('Digite um numero: ')
    
            # 2 - USA FUNCOES - RECEBE DADOS, MANIPULA DADOS, RETORNA DADOS

print(f'O valor digitado foi {n}')
print(type(n))







