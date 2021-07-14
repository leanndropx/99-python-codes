
# DESCREVE O EXERCICIO

print(''' PT - 01 - Um professor quer sortear um dos seus 4 alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome dos escolhidos''')
print()


# INICIALIZA O PROGRAMA

            # IMPORTA BIBLIOTECAS

import random

                # 1 - RECEBE DADOS
    

nome_estudante_1 = input('Digite o nome do primeiro estudante: ')
nome_estudante_2 = input('Digite o nome do segundo estudantet: ')
nome_estudante_3 = input('Digite o nome do terceiro estudante: ')
nome_estudante_4 = input('Digite o nome do quarto estudante: ')

lista_estudantes = [nome_estudante_1,nome_estudante_2,nome_estudante_3,nome_estudante_4]

    
                # 2 - MANIPULA E CRIA NOVOS DADOS


estudante_sorteado = random.choice(lista_estudantes)

                
                # 3 - DEVOLVE DADOS
        
print()
print(f'O estudante sorteado foi {estudante_sorteado}')



