import pygame as pg
from FunctionsTicTacToe import *

window = pg.display.set_mode((1000, 700)) #Primeiro Largura, depois altura
window.fill('#363636')

pg.font.init()
fonte = pg.font.SysFont('Times New Roman', 10)

board = [0,1,2,3,4,5,6,7,8]
#print(board)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
    
    mouse = pg.mouse.get_pos()
    mouse_position_x = mouse[0]
    mouse_position_y = mouse[1]

    
    click = pg.mouse.get_pressed()

    linhasTabuleiro(window)

    #teste de input
    
    pg.display.update()


