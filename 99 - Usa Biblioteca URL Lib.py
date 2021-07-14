    # - DESCREVENDO O DESAFIO
print('Desafio 99 - Crie um código Python que teste se o site Pudim está acessível pelo computador usado')
print()

    #INICIALIZANDO O PROGRAMA
    

        # IMPORTA BIBLIOTECAS

import urllib
import urllib.request


            # 1 - RECEBE DADOS, MANIPULA DADOS

try:
    site=urllib.request.urlopen('http://www.lorenclima.com.br')


            # 3 - DEVOLVE DAODS

except:
    print('O site Pudim não está funcionando')
else:
    print('O site Pudim está funcionando corretamente')
    print(site.read())










