'''
Создайте программу для игры в ""Крестики-нолики"" при помощи виртуального окружения и PIP
'''

import pygame as pg
import sys
from random import randint

def check_win(array, symbol):
    emty = 0
    for row in array:
        emty += row.count(0)
        if row.count(symbol) == 3:
            return f'Win {symbol}!'
    for col in range(3):
        if array[0][col] == symbol and array[1][col] == symbol and array[2][col] == symbol:
            return f'Win {symbol}!'
    if array[0][0] == symbol and array[1][1] == symbol and array[2][2] == symbol:
        return f'Win {symbol}!'
    if array[0][2] == symbol and array[1][1] == symbol and array[2][0] == symbol:
        return f'Win {symbol}!'
    if emty == 0:
        return 'Draw!'
    return False
pg.init()

screen_size = (300, 300)
screen = pg.display.set_mode((screen_size))
pg.display.set_caption('Крестики - нолики')
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)
black = (0, 0, 0)
margin = 10
size_block = 87
array = [[0 for _ in range(3)] for _ in range(3)]
counter = 0
game_over = False
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit(0)
        elif event.type == pg.MOUSEBUTTONDOWN and not game_over:
            x_mouse, y_mouse = pg.mouse.get_pos()
            column = x_mouse // (margin + size_block)
            row = y_mouse // (margin + size_block)
            if array[row][column] == 0:
                array[row][column] = 'x'
                counter += 1
        elif event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
            game_over = False
            array = [[0 for _ in range(3)] for _ in range(3)]
            counter = 0
            screen.fill(black)
        game_over = check_win(array, 'x')
        if game_over:
            break

        while counter % 2 and counter != 9:
            bot_r = randint(0, 2)
            bot_c = randint(0, 2)
            if array[bot_r][bot_c] == 0:
                array[bot_r][bot_c] = 'o'
                counter += 1
    if not game_over:
        for row in range(3):
            for col in range(3):
                if array[row][col] == 'x':
                    color = red
                elif array[row][col] == 'o':
                    color = green
                else:
                    color = white
                x = col * size_block + (col + 1) * margin
                y = row * size_block + (row + 1) * margin
                pg.draw.rect(screen, color, (x, y, size_block, size_block))
                if color == red:
                    pg.draw.line(screen, white, (x + 5, y + 5), (x + size_block - 5, y + size_block - 5), 5)
                    pg.draw.line(screen, white, (x + 5, y + size_block - 5), (x + size_block - 5, y + 5), 5)
                elif color == green:
                    pg.draw.circle(screen, white, (x + size_block // 2, y + size_block // 2), size_block // 2-3, 5)

    if (counter - 1) % 2:
        game_over = check_win(array, 'o')
    if game_over:
        screen.fill(black)
        font = pg.font.SysFont('stxingkai', 80)
        text_1 = font.render(game_over, True, white)
        text_rect = text_1.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2
        text_y = screen.get_height() / 2 - text_rect.height / 2
        screen.blit(text_1, [text_x, text_y])
    pg.display.update()