    # - DESCREVENDO O DESAFIO

print(''' 13 - Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar

    1 - Calcule o valor da prestaçõo mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado''')

    
    #INICIALIZANDO O PROGRAMA
    

        # IMPORTA BIBLIOTECAS



            # 1 - RECEBE DADOS

valor_da_casa = float(input('Quanto vale a casa hoje?: '))


salario = float(input('Qual o seu salário?: '))
trinta_porcento_do_salario = salario * 0.3


anos_para_quitar = int(input('Em quantos anos você pretende quitar?: '))
meses_para_quitar = anos_para_quitar * 12

valor_da_prestacao = valor_da_casa / meses_para_quitar




            # 2 - MANIPULA DADOS, RETORNA DADOS CONFORME CONDICAO

print()

if valor_da_prestacao <= trinta_porcento_do_salario:
        
        print(f'Parabéns, seu EMPRESTIMO foi APROVADO, o valor da prestação é de R$ {valor_da_prestacao:.2f}')


else:
        
        print('          EMPRESTIMO RECUSADO')
        print()

        print(f'1 - Com seu salario de R$ {salario:.2f} ,para uma casa no valor de R$ {valor_da_casa/1000:.0f} mil reais,')

        print(f'2 - o valor da prestação ficaria em R$ {valor_da_prestacao:.0f} , 00 ,')
    
        print(f'3 - portanto, excedendo R$ {valor_da_prestacao - trinta_porcento_do_salario:.2f} do valor permitido para seu salário')
    
        print(f'4 - o valor de 30% permitido para seu salário é de R$ {trinta_porcento_do_salario:.2f}.')



            





