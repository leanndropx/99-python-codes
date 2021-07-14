    # - DESCREVENDO O DESAFIO

print('35 - Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores M ou F',end='')
print('caso esteja errado, peça a digitação novamente até ter um valor correto')
print()



    #INICIALIZANDO O PROGRAMA
    

        # IMPORTA BIBLIOTECAS



            # 1 - RECEBE DADOS

sexo=str(input('digite seu sexo: ')).strip().upper()[0]

    
            # 2 - MANIPULA E CRIA NOVOS DADOS

while sexo not in 'MF':
    sexo=str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]

            
            # 3 - DEVOLVE DAODS

print('Sexo {} registrado com sucesso'.format(sexo))






