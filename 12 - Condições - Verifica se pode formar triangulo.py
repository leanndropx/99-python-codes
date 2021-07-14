
    # - DESCREVENDO O DESAFIO

print('''12 - Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se ela pode ou não formar um triângulo''')

print()

    #INICIALIZANDO O PROGRAMA
    

        # IMPORTA BIBLIOTECAS

import random
import statistics


            # 1 - RECEBE DADOS

lado_1 = int(input('Comprimento em CM da reta 1: '))
lado_2 = int(input('Comprimento em CM da reta 2: '))
lado_3 = int(input('Comprimento em CM da reta 3: '))

lista_com_lados = [lado_1,lado_2,lado_3]

            # 2 - MANIPULA DADOS, RETORNA DADOS CONFORME CONDICIONAL


lado_menor = min(lista_com_lados)
lado_maior = max(lista_com_lados)
for lado in lista_com_lados:
        if lado != lado_menor and lado != lado_maior:
          lado_mediano = lado


print()

if lado_maior < lado_menor + lado_mediano:
        
        print('É POSSIVEL formar um triângulo com as medidas informadas porque:')
        
        print()
        print(f'1 - o menor lado: {lado_menor}.')
        print(f'2 - + o lado mediano: {lado_mediano}.')
        print(f'3 - somados, correspondem a: {lado_menor + lado_mediano}.')
        print(f'4 - Portatno, a soma é maior do que o maior lado: {lado_maior}.')

else:

        print('NAO É POSSIVEL\033[m formar um triângulo porque:')
        
        print()
        print(f'1 - o menor lado: {lado_menor}.')
        print(f'2 - somado ao lado mediano: {lado_mediano}.')
        print(f'3 - corresponde a: {lado_menor + lado_mediano}.')
        print(f'4 - soma com valor menor do que o MAIOR lado: {lado_maior}.')








