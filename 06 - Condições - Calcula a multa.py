    
    # - DESCREVENDO O DESAFIO

print('''06 - Escreva um programa que leia a velocidade de um carro:
                
                1 - Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado
                2 - A multa vai custar 7,00 por cada km acima do limite''')
print()

    
    
    #INICIALIZANDO O PROGRAMA

        # - NAO HA BIBLIOTECAS PARA IMPORTAR


                # 1 - RECEBE DADOS
            
velocidade_do_carro = float(input('Digite a velocidade do carro em Km/hora: '))
velocidade_permitida = float(80)
multa_por_km = float(7)


            
                # 2 - MANIPULA DADOS RECEBIDOS E CRIA NOVOS DADOS

velocidade_ultrapassada = velocidade_do_carro - velocidade_permitida
multa_total = velocidade_ultrapassada * multa_por_km


            
                # 3 - RETORNA DADOS
            
print()
print(f'O carro estava a {velocidade_do_carro:.2f} km/hora, ultrapassando {velocidade_ultrapassada} km/hora da velocidade permitida')
print()

if velocidade_do_carro > velocidade_permitida:

        print(f'Você foi multado em \033[31m R${multa_total:.2f}\033[m reais')

else:
        print('Você dirigiu dentro da velocidade permitida')
