#Codigo Fonte: Jogo da Velha
#Programador: Caio Julio S. da Silva
#Terminal

from FunctionsTicTacToe import *

verificaContinua = 's'

textoObjetivo = """

--------------------TIC TAC TOE------------------------

instruções:

Jogo da Velha Classico
o jogo é constituido de uma tabela 3x3 detalhada com os indices disponiveis
em cada parte de tabela, assim, especificando quais indices são possiveis 
colocar o X ou O, ao longo da partida os simbolos X ou O irão
tomar o valor dos indices, de acordo com a escolha e partida efetuada
pelo jogadores.

tabela Modelo:

0 | 1 | 2
-----------
3 | 4 | 5
-----------
6 | 7 | 8

BOM JOGO !!!


"""

print(textoObjetivo)

while verificaContinua == 's':
    JogoDaVelha = [0,1,2,3,4,5,6,7,8]

    while True: #ESCOLHA DO PRIMEIRO JOGADOR

        primeiroItem = input('Primeiro Jogador, Escolha entre os itens, X ou O: ')
        escolha = EscolheItem(primeiroItem)

        if escolha == False:
            print('Item Invalido, Tente Novamente')
        else:
            if escolha[0] == 'X':
                print('\nSegundo Jogador, você ficou com o item " O " \n')
                break
            else:
                print('\nSegundo Jogador, você ficou com o item " X " \n')
                break
    
    print(f'Item Primeiro Jogador: {escolha[0]}')
    print(f'Item Segundo jogador: {escolha[1]}\n')

    for i in range(0, 9, 2):

        if i == 0:
            for apr in range(0, 7, 3): #Intevalo de 3 em 3 para valores de x = 0,3,6, apr significa apresentar, para ser apresentado o jogo sem nada preenchido pela primeira vez
                print(f'{JogoDaVelha[apr]} | {JogoDaVelha[apr+1]} | {JogoDaVelha[apr+2]}')

                if apr != 6:
                    print(f'-----------')
        
        while True:

            
            indice = int(input(f'Informe indice que você deseja substituir e lançar sua jogada:({escolha[0]}) '))
            verificaIndex = trataErroIndice(indice, JogoDaVelha)

            if verificaIndex == True:
                verificandoPosicao = verificaPosicao(indice, JogoDaVelha, escolha[0])

                if verificandoPosicao ==  False:
                    print('Posicao ja preenchida')
                else:
                    JogoDaVelha = verificandoPosicao
                    break
            else:
                print('indice invalido, tente novamente')
                
            

        for x in range(0, 7, 3): #Intevalo de 3 em 3 para valores de x = 0,3,6
            print(f'{JogoDaVelha[x]} | {JogoDaVelha[x+1]} | {JogoDaVelha[x+2]}')

            if x != 6:
                print(f'-----------')
        
        if i == 8:
            print('EMPATE')
            break

        #Tratamento de Vitória possivel:

        verificaResultado = TrataVitorias(f'{escolha[0]}', JogoDaVelha)

        if verificaResultado == True:
            print(f'Primeiro Jogador ({escolha[0]}) Venceu')
            break

        while True:

            indice = int(input(f'Informe indice que você deseja lançar sua jogada:({escolha[1]})'))
            verificaIndex = trataErroIndice(indice, JogoDaVelha)

            if verificaIndex == True:
                verificandoPosicao = verificaPosicao(indice, JogoDaVelha, escolha[1])

                if verificandoPosicao ==  False:
                    print('Posicao ja preenchida')
                else:
                    JogoDaVelha = verificandoPosicao
                    break
            else:
                print('indice invalido, tente novamente')

        for y in range(0, 7, 3): #Intevalo de 3 em 3 para valores de x = 0,3,6 print da lista
            print(f'{JogoDaVelha[y]} | {JogoDaVelha[y+1]} | {JogoDaVelha[y+2]}\n')

            if y != 8:
                print(f'-----------')

        #Tratamento de Vitória Possivel:

        verificaResultado = TrataVitorias(f'{escolha[1]}', JogoDaVelha)

        if verificaResultado == True:
            print(f'Segundo Jogador ({escolha[1]}) Venceu')
            break


    while True: 
        verificaContinua = input('deseja jogar novamente?:(s - SIM /n - NÃO):')

        if verificaContinua.lower() == 'n':
            print('----------OBRIGADO POR JOGAR--------')

        if verificaContinua.lower() != 's' and verificaContinua.lower() != 'n':
            print('Decisão Invalida, Tente Novamente!')
        else:
            break