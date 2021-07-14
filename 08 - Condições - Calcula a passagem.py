    
    # - DESCREVENDO O DESAFIO

print(''' 1 - Desafio 08 - Desenvolva um programa que pergunte a distância de uma viagem em KM.
          2 - Calcue o preço da passagem, cobrando 50 CENTAVOS por KM para viagens curtas de até 200 KM'
          3 - e 45 CENTAVOS para viagens mais longas.''')

    #INICIALIZANDO O PROGRAMA

        # IMPORTA BIBLIOTECAS

import random

                # 1 - RECEBE DADOS


distancia = random.randint(0,1000)

preco_km_viagens_curtas = 0.50
preco_km_viagens_longas = 0.45
    
                
                # 2 - MANIPULA DADOS

preco_total_viagens_curtas = distancia * preco_km_viagens_curtas
preco_total_viagens_longas = distancia * preco_km_viagens_longas

            
                
                # 3 - RETORNA DAODS

print(' ')
print(' A distância percorrida será de {} KM, então:'.format(distancia))

if distancia<=200:
    
        print('1 - Será cobrado {:.0f} centavos por Km rodado, porque'.format(preco_km_viagens_curtas * 100))
        print('2 - Foram percorridos menos de 200 Km, logo')
        print('3 - O preço da passagem é R${:.2f}'.format(preco_total_viagens_curtas))

else:
        print('1 - Será cobrado {:.0f} centavos por Km rodado, porque'.format(preco_km_viagens_longas * 100))
        print('2 - Foram percorridos mais de 200 km, logo')
        print('3 - O preço da passagem será R${:.2f}'. format(preco_total_viagens_longas))

