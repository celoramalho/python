import random
from tkinter import *


def tabuleiro(x, y):
    for i in range(0, 3):
        linha = []
        for j in range(0, 3):
            list.append(linha, 0)  #tabuleiro_xisoubolinha[i][j] = 0
        tabuleiro_xisoubolinha = tabuleiro_xisoubolinha + [linha]


def bot_escolha(tabuleiro):
    marcado = False

    while(not marcado):
        escolha_horizontal = random.randrange(3)
        escolha_vertical = random.randrange(3)
        escolha_horizontal = int(escolha_horizontal)
        escolha_vertical = int(escolha_vertical)

        pode_ou_nao_marcar = verifica_posicao_ocupada(escolha_horizontal, escolha_vertical, tabuleiro)

        if (pode_ou_nao_marcar):
            tabuleiro[escolha_horizontal][escolha_vertical] = 2
            marcado = True
        else:
            print("tentou")
    return tabuleiro

def jogador_escolha(tabuleiro):
    marcado = False

    while(not marcado):
        print("0 ->vazio\n1 -> jogado\n2 -> Computador")
        print(tabuleiro[0])
        print(tabuleiro[1])
        print(tabuleiro[2])

        escolha_horizontal = input("Linha: ")
        escolha_vertical = input("Coluna: ")
        escolha_horizontal = int(escolha_horizontal)
        escolha_vertical = int(escolha_vertical)

        pode_ou_nao_marcar = verifica_posicao_ocupada(escolha_horizontal, escolha_vertical, tabuleiro)

        if (pode_ou_nao_marcar):
            tabuleiro[escolha_horizontal][escolha_vertical] = 1
            marcado = True
        else:
            print("Posição já ocupada")
    return tabuleiro


def verifica_posicao_ocupada(x,y, tabuleiro):
    if (tabuleiro[x][y] == 0):
        return True
    else:
        return False

#def tk_interface():

def jogar():
    tabuleiro_xisoubolinha = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    acabou = False

    while(not acabou):
        tabuleiro_xisoubolinha = jogador_escolha(tabuleiro_xisoubolinha)
        tabuleiro_xisoubolinha = bot_escolha(tabuleiro_xisoubolinha)


if (__name__ == "__main__"):
    jogar()
