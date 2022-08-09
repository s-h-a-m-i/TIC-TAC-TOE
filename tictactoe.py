import pygame, sys
import numpy as np

pygame.init()

win=pygame.display.set_mode((600,600))
pygame.display.set_caption('TIC TAC TOE')
win.fill('#f5c3a9')

board = np.zeros((3,3))

width = 600
height = 600
line_width = 15
rows = 3
cols = 3
square_size = 200

x_color= (201, 79, 79)
o_color= (245, 98, 88)

def lines():
    pygame.draw.line(win, '#fce4d7', (0,200), (600,200), 10)
    pygame.draw.line(win, '#fce4d7', (0,400), (600,400), 10)

    pygame.draw.line(win, '#fce4d7', (200,0), (200,600), 10)
    pygame.draw.line(win, '#fce4d7', (400,0), (400,600), 10)

def draw():
    for row in range(3):
        for col in range(3):
            if board[row][col]==1:
                pygame.draw.circle(win, '#f56258', (int(col*200+100),int(row*200+100)), 60, 15)
            elif board[row][col]==2:
                pygame.draw.line(win, '#c94f4f', (col*200 + 50,row*200+200-50),(col*200+200-50, row*200+50), 25 )
                pygame.draw.line(win, '#c94f4f', (col*200 + 50,row*200+50),(col*200+200-50, row*200+200-50), 25 )

def mark(row, col, player):
    board[row][col] = player

def avail_square(row,col):
    return board[row][col] == 0

def board_full():
    for row in range(rows):
        for col in range(cols):
            if board[row][col] == 0:
                return False
    return True

def check_win(player):
    for col in range(cols):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical(col,player)
            return True
        
    for row in range(rows):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal(row,player)
            return True
        
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_rdiagonal(player)
        return True
    
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_ldiagonal(player)
        return True
    
    return False    

def draw_vertical(col,player):
    posX = col*200+100
    if player == 1:
        color = o_color
    elif player == 2:
        color = x_color
    
    pygame.draw.line(win, color, (posX, 15), (posX, 600-15), 15)

def draw_horizontal(row,player):
    posY = row*200+100
    if player == 1:
        color = o_color
    elif player == 2:
        color = x_color
        
    pygame.draw.line(win, color, (15, posY), (600-15, posY), 15)

def draw_ldiagonal(player):
    if player == 1:
        color = o_color
    elif player == 2:
        color = x_color
        
    pygame.draw.line(win, color, (15, 600 - 15), (600-15, 15), 15)

def draw_rdiagonal(player):
    if player == 1:
        color = o_color
    elif player == 2:
        color = x_color
        
    pygame.draw.line(win, color, (15, 15), (600-15, 600-15), 15)

def restart():
    win.fill('#f5c3a9')
    lines()
    player = 1
    for row in range(rows):
        for col in range(cols):
            board[row][col] = 0

lines()

player = 1
game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mousex = event.pos[0]
            mousey = event.pos[1]
            
            clicked_row = int(mousey//200)
            clicked_col = int(mousex//200)
            
            if avail_square(clicked_row, clicked_col):
                if player == 1:
                    mark(clicked_row, clicked_col, 1)
                    if check_win(player):
                        game_over = True
                    player = 2
                elif player == 2:
                    mark(clicked_row, clicked_col, 2)
                    if check_win(player):
                        game_over = True
                    player = 1
                
                draw()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()

    pygame.display.update()