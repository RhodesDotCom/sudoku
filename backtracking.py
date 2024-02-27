from pprint import pprint as pp


def find_empty(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col  # row, col

    return None


def valid(board, value, position):
    # check row
    for i in range(9):
        # if value is already in row, not including the value just inserted
        if board[position[0]][i] == value and position[1] != i:
            return False

    # check column
    for i in range(9):
        # if value is already in column, not including the value just inserted
        if board[i][position[1]] == value and position[0] != i:
            return False

    # check box
    row_index = position[0] // 3  # row in a 3x3 (0 --> 2)
    column_index = position[1] // 3  # column in a 3x3 (0 --> 2)
    for i in range(row_index * 3, row_index * 3 + 3):
        for j in range(column_index * 3, column_index * 3 + 3):
            if board[i][j] == value and (i, j) != position:
                return False

    return True


def solve(board):
    # board is solved once the board is filled
    found = find_empty(board)
    if not found:
        return True
    else:
        row, col = found
    for num in range(1, 10):
        if valid(board, num, (row, col)):  # check if number is valid
            board[row][col] = num  # if valid add to the board
            if solve(board):  # solve for new board if previous solve is valid
                return True  # return true to continue solving
            else:
                board[row][col] = 0  # if solution is invalid reset position to 0 and backtrack
    return False
