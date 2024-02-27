from backtracking import solve
from Solution_Checker import check_solution
from pprint import pprint as pp
import random

board = [[0]*9 for _ in range(9)]
solve(board)


def shuffle_rows(board):
    groups = [board[:3], board[3:6], board[6:]]
    for group in groups:
        random.shuffle(group)
    random.shuffle(groups)
    shuffled_board = [row for group in groups for row in group]
    return shuffled_board

def transpose(board):
    transposed_board = [[0]*9 for _ in range(9)]
    for row_index, row in enumerate(board):
        for value_index, value in enumerate(row):
            transposed_board[value_index][row_index] = value
    return transposed_board


board = shuffle_rows(board)
board = transpose(board)
board = shuffle_rows(board)
pp(board)
pp(check_solution(board))
