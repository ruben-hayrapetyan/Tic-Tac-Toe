#1. Create the window for our game
#2. Draw the grid where we'll play
#3. Draw the status bar to show which players' turn it is
#4. When someone wins, or its a draw, reset the game and say who won


import pygame as pg
from pygame.constants import *
import time

pg.init()
# CLOCK = pg.time.Clock()


XO = 'x'

winner = None
draw = False
height = 400
width = 400

white = (255, 255, 255)
line_color = (10, 10, 10)
TTT = [[None]*3, [None]*3, [None]*3]
screen = pg.display.set_mode([width, height + 100])

pg.display.set_caption('Tic Tac Toe')
opening = pg.image.load('/images/X.png')
X_image = pg.image.load('/images/X.png')
O_image = pg.image.load('/images/O.png')

opening = pg.transform.scale(opening, (width, height + 100))
X_image = pg.transform.scale(X_image, (80, 80))
O_image = pg.transform.scale(O_image, (80, 80))


def makegrid_and_gameopening():
    screen.blit(opening, (0, 0))
    pg.display.update()
    time.sleep(2)
    screen.fill(white)

    # drawing a grid
    pg.draw.line(screen, line_color, (width/3, 0), (width/3, height), 7)
    pg.draw.line(screen, line_color, (2/3*width, 0), (2/3*width, height), 7)
    pg.draw.line(screen, line_color, (0, height/3), (width, height/3), 7)
    pg.draw.line(screen, line_color, (0, 2/3*height), (width, 2/3*height), 7)
    draw_status_bar_writing()

def draw_status_bar_writing():
    global draw
    if winner is None:
        message = XO.upper() + "'s turn"
    else:
        message = winner.upper() + ' won'
    if draw:
        message = "None of y'all have won"

    font = pg.font.Font(None, 30)
    text = font.render(message, 1, white)

    screen.fill((0, 0, 0), (0, height, width, height + 100))
    text_rect = text.get_rect(center=(width/2, 450))
    screen.blit(text, text_rect)

    pg.display.update()

def check_winner():
    global winner, TTT, draw

    # check rows for a three in a row
    for row in range(0, 3):
        if (TTT[row][0] == TTT[row][1] == TTT[row][2]) and (TTT[row][0] is not None):
            winner = TTT[row][0]
            pg.draw.line(screen, (255, 0, 0), (0, (row+1) * height/3 - height/6),
                        (width, (row+1) * height/3 - height/6), 4)
        break

    #check columns for a three in a row
    for column in range (0,3):
        if (TTT[0][column] == TTT[1][column] == TTT[2][column]) and (TTT[0][column] is not None):
            winner = TTT[0][column]
            pg.draw.line(screen, (255, 0, 0), ((column + 1) * width / 3 - width / 6, 0),
                         ((column + 1) * width / 3 - width / 6, height), 4)
        break

    # checking the diagonals for three in a row (the left one)
    if (TTT[0][2] == TTT[1][1] == TTT[2][0]) and (TTT[0][2] is not None):
        winner = TTT[0][2]
        pg.draw.line(screen, (255, 0, 0), (350, 50), (50, 350), 4)

    # checking the diagonals for three in a row (the right one)
    if (TTT[0][0] == TTT[1][1] == TTT[2][2]) and (TTT[0][0] is not None):
        winner = TTT[0][0]
        pg.draw.line(screen, (255, 0, 0), (50, 50), (350, 350), 4)

    # checking all of the squares to see if it is a draw/tie
    if all([all(row) for row in TTT]) and winner is None:
        draw = True
    draw_status_bar_writing()


def draw_x_o(row, column):
    global TTT, XO
    if row == 1:
        posx = 30
    elif row == 2:
        posx = width/3 + 30
    elif row == 3:
        posx = width/3 * 2 +30

    if column == 1:
        posy = 30
    elif column == 2:
        posy = height/3 + 30
    elif column == 3:
        posy = height/ 3 * 2 + 30

    TTT[row - 1][column - 1] = XO
    if XO == 'x':
        screen.blit(X_image, (posy, posx))
        XO = 'o'
    else:
        screen.blit(O_image, (posy, posx))
        XO = 'x'
    pg.display.update()


def userCLick():
    # Getting coordinates of mouse click
    x, y = pg.mouse.get_pos()

    # Getting the column of mouse click
    if x < width/3:
        column = 1
    elif x < width/3 * 2:
        column = 2
    elif x < width:
        column = 3
    else:
        column = None

    # Getting the row of mouse click
    if y < height/ 3:
        row = 1
    elif y < height/ 3 * 2:
        row = 2
    elif y < height:
        row = 3
    else:
        row = None

    # Calling Draw
    if row and column and TTT[row - 1][column - 1] is None:
        global XO
        draw_x_o(row, column)
        check_winner()

def reset_game():
    global TTT, XO, winner, draw
    time.sleep(2)
    XO = 'x'
    winner = None
    draw = False
    TTT = [[None] * 3, [None] * 3, [None] * 3]
    makegrid_and_gameopening()

def main():
    makegrid_and_gameopening()
    while True:
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
            elif event.type == MOUSEBUTTONDOWN:
                userCLick()
                if winner or draw:
                    reset_game()



        pg.display.update()


if __name__ == '__main__':
    main()


