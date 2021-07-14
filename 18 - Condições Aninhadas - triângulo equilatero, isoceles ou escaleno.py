
    # - DESCREVENDO O DESAFIO

print('Desafio do triângulo 18 - Desenvolva um programa que leia o comprimento de três retas e diga ao usuário',end='')
print('se ela pode ou não formar um triângulo')
print('  ')

print('Desafio 42 - Refaça o desafio dos triângulos, acrescentando o recurso de mostrar',end='')
print('que tipo de triângulo será formado:')
print('1 - Equilátero: todos os lados iguais')
print('2 - Isóceles: dois lados iguais')
print('3 - Escaleno: todos os lados diferentes')
print()

    #INICIALIZANDO O PROGRAMA
    
        # IMPORTA BIBLIOTECAS

import random
import statistics

            # 1 - RECEBE DADOS


reta_1 = int(input('Comprimento da reta 1: '))
reta_2 = int(input('Comprimento da reta 2: '))
reta_3 = int(input('Comprimento da reta 3: '))



            # 2 - MANIPULA DADOS, CRIA NOVOS DADOS


pode_formar_triangulo = reta_1 < reta_2 + reta_3


equilatero =    reta_1 == reta_2 and reta_2 == reta_3

isoceles = reta_1 == reta_2 and reta_1 != reta_3    or      reta_2 == reta_3 and reta_2 != reta_1   or      reta_3 == reta_1 and reta_3 != reta_2

escaleno =     reta_1 != reta_2 and reta_2 != reta_3 and reta_3 != reta_1


lista = [reta_1,reta_2,reta_3]


            
            # 2 - RETORNA DADOS CONFORME CONDICAO
    
            
if pode_formar_triangulo and equilatero:
    
    print('1 - O triângulo é equilátero, pois todos os lados são iguais')

elif pode_formar_triangulo and isoceles:
    
    print('2 - O triângulo é ISOCELES')

elif pode_formar_triangulo and escaleno:
    
    print('3 - O triângulo é ESCALENO')

else:
    
    print('As medidas dos lados não podem formar um triângulo porque:')
    
    print('1 - a reta {} com maior lado: {}'.format('3' if reta_3==max(lista) else '',max(lista)))
    
    print('2 - é maior ou igual do que a soma dos outros dois: {}'.format(statistics.median(lista)+min(lista)))

  

