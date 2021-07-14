
    # - DESCREVENDO O DESAFIO

print('41 - Melhore o desafio 61, perguntando para o usuário se ele quer mostrar mais alguns termos',end='')
print('o programa encerra quando ele disser que quer mostrar 0 termos')
print()

    #INICIALIZANDO O PROGRAMA
    

        # IMPORTA BIBLIOTECAS



            # 1 - RECEBE DADOS

primeiro_termo = int(input('digite o primeiro termo: '))
razao = int(input('digite a razão: '))

contador=1
total_de_termos = 0
mais_quantos_termos = 10
    
            
            # 2 - MANIPULA E CRIA NOVOS DADOS

while mais_quantos_termos != 0:
    
    total_de_termos = total_de_termos + mais_quantos_termos
    
    ultimo_termo = primeiro_termo + (razao * total_de_termos)

    while contador <= total_de_termos:
        
        print(primeiro_termo,end=' ')
        
        print(' < ' if primeiro_termo < ultimo_termo-1 else '',end=' ')
        
        primeiro_termo = primeiro_termo + razao
        
        contador=contador+1
    
    print('PAUSA')
    mais_quantos_termos = int(input('\nGostaria de mostrar mais quantos termos?: '))
            
            # 3 - DEVOLVE DAODS

print('Foram mostrados {}{}{} termos'.format('\033[35m',total_de_termos,'\033[35m'))

