
# DESCREVE O DESAFIO

print('PT - 03 - Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3')
print()

# INICIALIZA O PROGRAMA

        # IMPORTA BIBLIOTECAS

import pygame

            # 1 - RECEBE DADOS

# - 'nome.audio.mp3' precisa ser adicionado ao abiente de desenvolvimento
        
            # 2 - MANIPULA E CRIA NOVOS DADOS

pygame.init()
pygame.mixer.music.load('nome_audio.mp3')
pygame.mixer.music.play()
pygame.event.wait()

            # 3 - DEVOLVE DADOS

# - 'nome.audio.mp3 será reproduzido.

