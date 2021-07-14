
    # - DESCREVENDO O DESAFIO

print('19 - Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC',end='')
print('e mostre seu status, de acordo com a tabela abaixo:')

print('1 - Abaixo de 18.5: abaixo do peso')
print('2 - Entre 18.5 e 25: peso ideal')
print('3 - 25 até 30: sobrepeso')
print('4 - 30 até 40: obesidade')
print('5 - acima de 40: obesidade mórbida')

print()


    #INICIALIZANDO O PROGRAMA
    

        # IMPORTA BIBLIOTECAS

from math import ceil


            # 1 - RECEBE DADOS


nome = input('Digite seu nome: ')

peso = float(input('Digite seu peso: '))

altura = float(input('Digite sua altura: '))

    
            # 2 - MANIPULA E CRIA NOVOS DADOS


imc = peso/(altura**2)

            
            # 3 - DEVOLVE DAODS


if imc < 18.5:
    
        print('1 - Você está abaixo do peso, {}'.format(nome))
    
        print('2 - Seu IMC é {:.2f}'.format(imc))


elif imc >= 18.5 and imc <= 25:
    
        print('1 - Você está com o peso ideal, {}'.format(nome))
    
        print('2 - Seu IMC é {:.2f}'.format(imc))


elif imc > 25 and imc <= 30:
    
        print('1 - Você está com sobrepeso, {}'.format(nome))
    
        print('2 - Seu IMC é {:.2f}'.format(imc))
    
        print('3 - Você está passando {} pontos do IMC ideal'.format(imc-25))
    
        print('4 - Perca {} kg para chegar no IMC máximo ideal'.format(ceil((imc-25)/0.35)))
    
        print('5 - Perca {} kg para chegar no IMC mínimo ideal'.format( ceil((imc-22)/0.35)))



elif imc > 30 and imc <= 40:
        
        print('1 - Você está com obesidade, {}'.format(nome))
        
        print('2 - Seu IMC é {:.2f}'.format(imc))


else:
        print('1 - {}, seu caso é grave, você está com obesidade mórbida'.format(nome))
    
        print('2 - Seu IMC é {:.2f}'.format(imc))
    
        print('3 - Você está passando {:.2f} pontos do IMC ideal'.format(imc-25))
    
        print('4 - O ideal é que você perca pelo menos {:.2f} kilos para alcançar o IMC ideal'.format((imc-25)/0.35))








