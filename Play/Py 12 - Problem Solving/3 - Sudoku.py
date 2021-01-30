# Created on January, 2021
# @author: Fábio Araújo de Sá

def find_all_zeros(board):

    alist = []

    for x in range(len(board[0])):
        for y in range(len(board)):

            if board[x][y] == 0:
                atuple = tuple((x, y))
                alist.append(atuple)

    return alist

def is_row(board, coordinate, possibilities):
    
    row = board[coordinate[0]]
    value = sum(possibilities) - sum(row)
    
    return value, row

def is_column(board, coordinate, possibilities):

    column = [board[x][coordinate[1]] for x in range(len(board))]
    value = sum(possibilities) - sum(column)

    return value, column

def is_square(board, coordinate, possibilities):

    def which_quadrant(coordinate, board):
    
        y, x = coordinate

        # Q == (1 or 2 or 3)
        if y < 3:
            if x < 3:
                return list([board[0][0], board[0][1], board[0][2], board[1][0], board[1][1], board[1][2], board[2][0], board[2][1], board[2][2]])
            if x >= 3 and x < 6:
                return list([board[0][3], board[0][4], board[0][5], board[1][3], board[1][4], board[1][5], board[2][3], board[2][4], board[2][5]])
            if x >= 6 and x < 9:
                return list([board[0][6], board[0][7], board[0][8], board[1][6], board[1][7], board[1][8], board[2][6], board[2][7], board[2][8]])

        # Q == (4 or 5 or 6)
        if y >= 3 and y < 6:
            if x < 3:
                return list([board[3][0], board[3][1], board[3][2], board[4][0], board[4][1], board[4][2], board[5][0], board[5][1], board[5][2]])
            if x >= 3 and x < 6:
                return list([board[3][3], board[3][4], board[3][5], board[4][3], board[4][4], board[4][5], board[5][3], board[5][4], board[5][5]])
            if x >= 6 and x < 9:
                return list([board[3][6], board[3][7], board[3][8], board[4][6], board[4][7], board[4][8], board[5][6], board[5][7], board[5][8]])

        # Q == (7 or 8 or 9)        
        if y >= 6 and y < 9:
            if x < 3:
                return list([board[6][0], board[6][1], board[6][2], board[7][0], board[7][1], board[7][2], board[8][0], board[8][1], board[8][2]])
            if x >= 3 and x < 6:
                return list([board[6][3], board[6][4], board[6][5], board[7][3], board[7][4], board[7][5], board[8][3], board[8][4], board[8][5]])
            if x >= 6 and x < 9:
                return list([board[6][6], board[6][7], board[6][8], board[7][6], board[7][7], board[7][8], board[8][6], board[8][7], board[8][8]])

        return "Error!"

    square = which_quadrant(coordinate, board)
    value = sum(possibilities) - sum(square)

    return value, square

def solve_sudoku(board):

    possibilities = list([x for x in range(1, 10)])
    all_zeros = find_all_zeros(board)

    for coordinate in all_zeros:

        vc, column = is_column(board, coordinate, possibilities)
        vr, row = is_row(board, coordinate, possibilities)
        vs, square = is_square(board, coordinate, possibilities)

        if vs != 0 and vs not in square:
            board[coordinate[0]][coordinate[1]] = vs   

        if vr != 0 and vr not in row:
            board[coordinate[0]][coordinate[1]] = vr   

        if vc != 0 and vc not in column:
            board[coordinate[0]][coordinate[1]] = vc

    return board

board =[[9, 3, 7, 1, 4, 2, 5, 8, 6], 
        [5, 6, 2, 7, 3, 8, 1, 4, 0], 
        [4, 8, 1, 9, 5, 6, 7, 2, 3], 
        [1, 4, 6, 0, 9, 3, 8, 5, 0], 
        [3, 2, 5, 6, 8, 7, 9, 1, 4], 
        [8, 7, 9, 4, 0, 5, 3, 6, 2], 
        [7, 9, 4, 8, 2, 1, 6, 3, 5], 
        [6, 5, 8, 3, 7, 4, 2, 9, 1], 
        [2, 1, 3, 5, 6, 9, 4, 7, 8]]

print(solve_sudoku(board))
