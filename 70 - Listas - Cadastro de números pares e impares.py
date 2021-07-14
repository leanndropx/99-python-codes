    # - DESCREVENDO O DESAFIO
print('70 - Crie um programa onde o usuário possa digitar 7 valores numéricos',end='')
print('e cadastre-os em uma lista única que mantenha separado os valores pares e impares.')
print('No final, mostre os valores pares e impares em ordem crescente')
print()

    #INICIALIZANDO O PROGRAMA
    

        # IMPORTA BIBLIOTECAS



            # 1 - RECEBE DADOS

valores=list()
pares=list()
impares=list()
for c in range(0,7):
    n=int(input('digite um numero: '))


            # 2 - MANIPULA E CRIA NOVOS DADOS

    if n%2==0:
        pares.append(n)
    else:
        impares.append(n)

valores.append(sorted(pares))
valores.append(sorted(impares))

            
            # 3 - DEVOLVE DAODS

print(valores)
