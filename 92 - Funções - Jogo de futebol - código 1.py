    # - DESCREVENDO O DESAFIO
print('Desafio 92 - Faça um programa que tenha uma função chamada ficha(), que receba dois parametros',end='')
print('opcionais: o nome do jogador e quantos gols ele marcou.')
print('O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido',end='')
print('informado corretamente')

    #INICIALIZANDO O PROGRAMA
    

        # IMPORTA BIBLIOTECAS


        # CRIA FUNCOES
        
def ficha(nome='<desconhecido>',gols=0):
    gols=str(gols)
    if len(nome)==0:
        nome='<desconhecido>'
    if len(gols)==0:
        gols=0
    print(f'O jogador {nome} fez {gols} gols no campeonato')

                        
            # 1 - RECEBE DADOS

nome=str(input('nome: '))
gols=str(input('quantos gols?: '))

    
            # 2 - USA FUNCOES - RECEBE DADOS, MANIPULA DADOS, RETORNA DADOS


ficha(nome,gols)
ficha('Mateus',7)
ficha()

