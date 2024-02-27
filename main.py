import pygame
from tkinter import *
from tkinter import messagebox
from Solution_Checker import check_solution
from generator import generate_board
from backtracking import solve

pygame.init()

WIDTH, HEIGHT = 500, 600
GRID_EDGE = 450
inc = GRID_EDGE / 9
pos0_x, pos0_y = 25, 50  # coords of original_gameboard in window
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")

FPS = 60

GREY = (128, 128, 128)  # background
LIGHT_GREY = (192, 192, 192)  # highlight
WHITE = (255, 255, 255)  # text
BLACK = (0, 0, 0)  # original_gameboard lines
RED = (170, 0, 0)  # original values
BLUE = (0, 153, 153)

THICK_LINE = 3
THIN_LINE = 1

difficulty = 25
original_gameboard = generate_board(difficulty)


def draw_vertical():
    for i in range(10):
        if i % 3 == 0:
            pygame.draw.line(surface=WINDOW,
                             color=BLACK,
                             start_pos=(pos0_x + i / 9 * GRID_EDGE, pos0_y),
                             end_pos=(pos0_x + i / 9 * GRID_EDGE, pos0_y + GRID_EDGE),
                             width=THICK_LINE
                             )
        else:
            pygame.draw.line(surface=WINDOW,
                             color=BLACK,
                             start_pos=(pos0_x + i / 9 * GRID_EDGE, pos0_y),
                             end_pos=(pos0_x + i / 9 * GRID_EDGE, pos0_y + GRID_EDGE),
                             width=THIN_LINE
                             )


def draw_horizontal():
    for i in range(10):
        if i % 3 == 0:
            pygame.draw.line(surface=WINDOW,
                             color=BLACK,
                             start_pos=(pos0_x, pos0_y + i / 9 * GRID_EDGE),
                             end_pos=(pos0_x + GRID_EDGE, pos0_y + i / 9 * GRID_EDGE),
                             width=THICK_LINE
                             )
        else:
            pygame.draw.line(surface=WINDOW,
                             color=BLACK,
                             start_pos=(pos0_x, pos0_y + i / 9 * GRID_EDGE),
                             end_pos=(pos0_x + GRID_EDGE, pos0_y + i / 9 * GRID_EDGE),
                             width=THIN_LINE
                             )


def add_buttons():
    pygame.font.init()
    font = pygame.font.SysFont("arialblack", 15)

    check_button_pos = (25, 525)
    complete_button_pos = (180, 525)
    clear_button_pos = (335, 525)
    button_size = (140, 50)
    check_button = pygame.Rect(check_button_pos, button_size)
    complete_button = pygame.Rect(complete_button_pos, button_size)
    clear_button = pygame.Rect(clear_button_pos, button_size)

    check_text = font.render('Check Solution', True, WHITE)
    complete_text = font.render('Auto-complete', True, WHITE)
    clear_text = font.render('Reset Board', True, WHITE)

    check_text_size = font.size('Check Solution')
    comp_text_size = font.size('Auto-complete')
    clear_text_size = font.size('Reset Board')

    check_pos_add_x = (button_size[0] - check_text_size[0]) / 2
    check_pos_add_y = (button_size[-1] - check_text_size[-1]) / 2

    comp_pos_add_x = (button_size[0] - comp_text_size[0]) / 2
    comp_pos_add_y = (button_size[-1] - comp_text_size[-1]) / 2

    clear_pos_add_x = (button_size[0] - clear_text_size[0]) / 2
    clear_pos_add_y = (button_size[-1] - clear_text_size[-1]) / 2

    check_text_pos = (check_button_pos[0] + check_pos_add_x,
                      check_button_pos[-1] + check_pos_add_y)
    comp_text_pos = (complete_button_pos[0] + comp_pos_add_x,
                      complete_button_pos[-1] + comp_pos_add_y)
    clear_text_pos = (clear_button_pos[0] + clear_pos_add_x,
                      clear_button_pos[-1] + clear_pos_add_y)

    pygame.draw.rect(WINDOW, LIGHT_GREY, check_button)
    pygame.draw.rect(WINDOW, LIGHT_GREY, complete_button)
    pygame.draw.rect(WINDOW, LIGHT_GREY, clear_button)

    WINDOW.blit(source=check_text, dest=check_text_pos)
    WINDOW.blit(source=complete_text, dest=comp_text_pos)
    WINDOW.blit(source=clear_text, dest=clear_text_pos)


def fill_values(gameboard):
    pygame.font.init()
    font = pygame.font.SysFont("arialblack", 30)

    for y in range(9):
        for x in range(9):
            if gameboard[y][x] != 0:
                number = str(gameboard[y][x])
                text = font.render(number, True, WHITE)
                size = font.size(number)
                draw_x = pos0_x + (x * inc) + (inc / 2 - size[0] / 2)
                draw_y = pos0_y + (y * inc) + (inc / 2 - size[1] / 2)

                WINDOW.blit(source=text,
                            dest=(draw_x, draw_y)
                            )


def restore_existing_values(original_board, working_board):
    new_board = [[0] * 9 for _ in range(9)]
    for y, row in enumerate(original_board):
        for x, value in enumerate(row):
            if value != 0:
                new_board[y][x] = value
            elif value == 0 and working_board[y][x] != 0:
                new_board[y][x] = working_board[y][x]
    return new_board


def select_cell(mouse_pos):
    if 25 < mouse_pos[0] < 475 and 50 < mouse_pos[1] < 500:
        grid_pos = ((mouse_pos[0] - 25) // 50, (mouse_pos[-1] - 50) // 50)
        draw_x = pos0_x + grid_pos[0] * inc
        draw_y = pos0_y + grid_pos[-1] * inc
        pos = (draw_x, draw_y)
        size = (inc, inc)
        highlight = pygame.Rect(pos, size)
        pygame.draw.rect(WINDOW, LIGHT_GREY, highlight)
        pygame.display.update()
        return grid_pos


def get_keypress():
    val = -1
    flag = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                    val = 1
                if event.key == pygame.K_2 or event.key == pygame.K_KP2:
                    val = 2
                if event.key == pygame.K_3 or event.key == pygame.K_KP3:
                    val = 3
                if event.key == pygame.K_4 or event.key == pygame.K_KP4:
                    val = 4
                if event.key == pygame.K_5 or event.key == pygame.K_KP5:
                    val = 5
                if event.key == pygame.K_6 or event.key == pygame.K_KP6:
                    val = 6
                if event.key == pygame.K_7 or event.key == pygame.K_KP7:
                    val = 7
                if event.key == pygame.K_8 or event.key == pygame.K_KP8:
                    val = 8
                if event.key == pygame.K_9 or event.key == pygame.K_KP9:
                    val = 9
                if event.key == pygame.K_BACKSPACE:
                    val = 0
                    flag = 1
                if event.key == pygame.K_ESCAPE:
                    flag = 1
        if flag == 1 or val > 0:
            return val


def clear_board(gameboard):
    if messagebox.askyesno(message='Are you sure you want to clear the board'):
        return original_gameboard
    else:
        return gameboard


def check_complete(gameboard):
    flag = False
    for row in gameboard:
        for value in row:
            if value == 0:
                flag = True
    if flag:
        messagebox.showinfo(message='board is incomplete')
        return False
    else:
        if messagebox.askyesno(message='Are you ready to submit your board'):
            return True
        else:
            return False


def complete():
    if messagebox.askyesno(title='Congrats!',
                           message='would you like a new puzzle? (press no to quit)'):
        return generate_board(difficulty)
    else:
        pygame.quit()




def set_gameboard(board):
    WINDOW.fill(GREY)
    draw_vertical()
    draw_horizontal()
    fill_values(board)
    add_buttons()
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    set_gameboard(original_gameboard)
    gameboard = original_gameboard
    run = True
    while run:
        clock.tick(FPS)

        gameboard = restore_existing_values(original_gameboard, gameboard)
        set_gameboard(gameboard)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                # check whether a cell has been clicked
                if (pos0_x < mouse_pos[0] < (pos0_x + GRID_EDGE)) and (pos0_y < mouse_pos[-1] < (pos0_y + GRID_EDGE)):
                    cell = select_cell(mouse_pos)
                    val = get_keypress()
                    if val > -1:
                        gameboard[cell[-1]][cell[0]] = val
                # Check solution button pressed
                elif (25 < mouse_pos[0] < 165) and (525 < mouse_pos[-1] < 575):
                    check_flag = check_complete(gameboard)
                    if check_flag:
                        if check_solution(gameboard):
                            gameboard = complete()
                        else:
                            # add option to give up or retry
                            print('incorrect')
                # check if auto-complete button is pressed
                elif (180 < mouse_pos[0] < 320) and (525 < mouse_pos[-1] < 575):
                    solve(gameboard)

                # check if clear button is pressed
                elif (335 < mouse_pos[0] < 475) and (525 < mouse_pos[-1] < 575):
                    gameboard = clear_board(gameboard)

    pygame.quit()


if __name__ == "__main__":
    main()
