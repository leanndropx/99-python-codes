    # - DESCREVENDO O DESAFIO
print('Deafio 97 - Faça um mini sistema que use o Interactive  Help do Python. O usuário vai ',end='')
print('digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra FIM, o programa encerrará.')
print('OBS: Use cores')
print()

    #INICIALIZANDO O PROGRAMA
    

        # IMPORTA BIBLIOTECAS


        # CRIA FUNCOES
        
def titulo(msg,cor=0):
    print(c[cor],end='')
    print('*'*(len(msg)+4))
    print(f'  {msg}')
    print('*' * (len(msg) + 4))
    print('\033[m',end='')

def ajuda(comando):
    titulo(f'ACESSANDO O MANUAL DO COMANDO {comando}',5)
    sleep(1)
    help(comando)
    sleep(0.3)

                        
            # 1 - RECEBE DADOS

c=('\033[30m',      #0 - sem cor
   '\033[7;31m',    #1 - vermelho
   '\033[7;32m',    #2 - verde
   '\033[7;33m',    #3 - amarelo
   '\033[7;34m',    #4 - azul
   '\033[7;35m')    #5 - lilas

    
            # 2 - USA FUNCOES - RECEBE DADOS, MANIPULA DADOS, RETORNA DADOS


while True:
    sleep(0.3)
    titulo('SISTEMA DE AJUDA PyHELP',2)
    sleep(0.3)
    comando=str(input('Função ou biblioteca: '))
    sleep(0.5)
    ajuda(comando)
    sleep(0.5)
    if comando==str(0):
        titulo('Finalizando o sistema...',3)
        sleep(0.3)
        titulo('ATE LOGO',1)
        break
