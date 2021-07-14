    # - DESCREVENDO O DESAFIO
print('Desafio 93 - Faça um programa que tenha uma função chamada ficha(), que receba dois parametros',end='')
print('opcionais: o nome do jogador e quantos gols ele marcou.')
print('O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido',end='')
print('informado corretamente')
print()

    #INICIALIZANDO O PROGRAMA
    

        # IMPORTA BIBLIOTECAS


        # CRIA FUNCOES
        

                        
            # 1 - RECEBE DADOS


    
            # 2 - USA FUNCOES - RECEBE DADOS, MANIPULA DADOS, RETORNA DADOS






def ficha(nome='<desconhecido>',gols=0):
    print(f'O jogador {nome} marcou {gols} gols')

nome=str(input('nome do jogador: '))
gols=str(input('quantidade de gols: '))

if nome.strip()=='':
    ficha(nome='<desconhecido>')
elif gols.isnumeric():
    gols=int(gols)
    ficha(nome,gols)
else:
    gols=0
    ficha(nome,gols)





