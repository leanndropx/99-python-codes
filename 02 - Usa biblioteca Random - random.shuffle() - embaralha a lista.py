
# DESCREVE DESAFIO

print('''PT - Um professor quer sortear a ordem de apresentação entre seus 4 alunos.''')
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
print()
    
            # 2 - MANIPULA E CRIA NOVOS DADOS

sorteia_ordem_apresentacao = random.shuffle(lista_estudantes)      # - shuffle embaralha uma lista

            
            # 3 - DEVOLVE DAODS
            
print(f'A ordem de apresentação será {sorteia_ordem_apresentacao}')


