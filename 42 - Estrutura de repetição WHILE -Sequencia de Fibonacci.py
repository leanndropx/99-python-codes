
    # - DESCREVENDO O DESAFIO

print('42 - Escreva um programa que leia um numero n inteiro',end='')
print('e mostre na tela os n primeiros elementos de uma sequencia de Fibonacci')
print('   >  sequencia de fibonacci: cada termo subsequente corresponde a soma dos dois anteriores')
print()
print()


    #INICIALIZANDO O PROGRAMA
    

        # IMPORTA BIBLIOTECAS



            # 1 - RECEBE DADOS

quantidade_de_termos = int(input('quantos termos você quer mostrar?: '))

primeiro_termo = 0
segundo_termo = 1

print (f'{primeiro_termo}  >  {segundo_termo}',end=' ')

contador = 3

            # 2 - MANIPULA DADOS, RETORNA DADOS

while contador <= quantidade_de_termos:
    
    terceiro_termo = primeiro_termo + segundo_termo
    print(' > ',end=' ')
    print(f'{terceiro_termo}',end=' ')
    
    primeiro_termo = segundo_termo
    segundo_termo = terceiro_termo
    
    contador = contador+1








