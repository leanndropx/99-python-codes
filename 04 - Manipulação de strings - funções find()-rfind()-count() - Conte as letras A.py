
# - DESCREVENDO O DESAFIO

print('''04 - Faça um programa que leia uma frase pelo teclado e mostre:
                1 - Quantas vezes aparece a letra A
                2 - Em que posição ela aparece a primeira vez
                3 - Em que posição ela aparece a ultima vez''')
print()


    #INICIALIZANDO O PROGRAMA
    
                # 1 - RECEBE DADOS
        
frase=input('Digite uma frase: ').strip()


                # 2 - MANIPULA E CRIA NOVOS DADOS

contagem_letras_a = frase.lower().count("a")
posicao_primeira_letra_a = frase.upper().find("A")+1
posicao_ultima_letra_a = frase.upper().rfind("A")+1


                # 3 - DEVOLVE DADOS

print()
print(f'1 - A letra A aparece {contagem_letras_a} vezes')
print(f'2 - Ela aparece a primeira vez na posição {posicao_primeira_letra_a}')
print(f'3 - Ele aparece a última vez na posição {posicao_ultima_letra_a}')



