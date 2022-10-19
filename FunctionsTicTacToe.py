#documentos com funções utilizadas no projeto de criação de jogo da velha para terminal, o intuito é reutilizar as mesmas funções criadas sem chamar o programa inteiro

#funções necessarias para o terminal

def TrataVitorias(valor, jgdavelha):

    """
    Função verifica se há vitoria da Bolinha ou do Xis

    """

    if jgdavelha[0] == valor and jgdavelha[1] == valor and jgdavelha[2] == valor:
        return True
    elif jgdavelha[3] == valor and jgdavelha[4] == valor and jgdavelha[5] == valor:
        return True
    elif jgdavelha[6] == valor and jgdavelha[7] == valor and jgdavelha[8] ==valor:
        return True
    elif jgdavelha[0] == valor and jgdavelha[3] == valor and jgdavelha[6] == valor:
        return True
    elif jgdavelha[1] == valor and jgdavelha[4] == valor and jgdavelha[7] ==valor:
        return True
    elif jgdavelha[2] == valor and jgdavelha[5] == valor and jgdavelha[8] ==valor:
        return True
    elif jgdavelha[0] == valor and jgdavelha[4] == valor and jgdavelha[8] ==valor:
        return True
    elif jgdavelha[2] == valor and jgdavelha[4] == valor and jgdavelha[6] ==valor:
        return True
    else:
        return False

def trataErroIndice(jogada, jgdavelha):

    """
    Função verifica se há IndexError, e faz o retorno devido
    """

    try:
        
        if jogada < len(jgdavelha):
            return True

    except IndexError:
        return False   

def EscolheItem(primeiroJogador):

    """
    Função valida item fornecido pelo usuario
    """

    if primeiroJogador.upper() != 'X' and primeiroJogador.upper() != 'O':
        return False
    else:
        if primeiroJogador == 'X':
            segundoJogador = 'O'
            return primeiroJogador, segundoJogador
        else:
            segundoJogador = 'X'
            return primeiroJogador, segundoJogador

def verificaPosicao(indice, jgdavelha, jogador):

    """
    Função verifica se ha algum X ou O na posição desejada
    """

    if 'O' == jgdavelha[indice] or 'X' == jgdavelha[indice]: 
        return False
    else:
        jgdavelha[indice] = f'{jogador}'
        return jgdavelha

#funções necessarias para a interface grafica pygame (EM DESENVOLVIMENTO)

import pygame as pg

def linhasTabuleiro(window):


    #linhas verticais

    pg.draw.line(window, (248,248,255), (170, 100), (170, 545), 13)
    pg.draw.line(window, (248,248,255), (300, 100), (300, 545), 13)

    #linhas Horizontais

    pg.draw.line(window, (248,248,255), (40, 230), (440, 230), 13)
    pg.draw.line(window, (248,248,255), (40, 390), (440, 390), 13) #argumentos: janela criada, cor, x,y(inicio da linha), x,y(termino da linha), espessura da linha
