# Created on January, 2021
# @author: Fábio Araújo de Sá

def is_column(board):

    for possible_winner in [1, 2]:
        for c in range(len(board[0])):
            for r in range(len(board)-3):

                if board[r][c] == board[r+1][c] == board[r+2][c] == board[r+3][c]:
                    if board[r][c] == possible_winner:
                        return tuple((r, c))

    return False

def is_row(board):

    for possible_winner in [1, 2]:
        for c in range(len(board[0])-3):
            for r in range(len(board)):

                if board[r][c] == board[r][c+1] == board[r][c+2] == board[r][c+3]:
                    if board[r][c] == possible_winner:
                        return tuple((r, c))  

    return False

def is_diagonal(board):

    def diagonal_positiva(board):

        for possible_winner in [1, 2]:
            for c in range(len(board[0])-3):
                for r in range(len(board)-3):

                    if board[r][c] == board[r+1][c+1] == board[r+2][c+2] == board[r+3][c+3]:
                        if board[r][c] == possible_winner:
                            return tuple(("positiva", r, c))

        return False

    def diagonal_negativa(board):
        
        for possible_winner in [1, 2]:
            for c in range(len(board[0])-3):
                for r in range(3, len(board)):

                    if board[r][c] == board[r-1][c+1] == board[r-2][c+2] == board[r-3][c+3]:
                        if board[r][c] == possible_winner:
                            return tuple(("negativa", r, c))
        
        return False 

    return diagonal_positiva(board) if diagonal_positiva(board) != False else diagonal_negativa(board)

def four_in_line(board):

    result = set()

    if is_column(board) != False:

        x, y = is_column(board)

        result.add((x, y))
        result.add((x+3, y))

    if is_row(board) != False:

        x, y = is_row(board)

        result.add((x, y))
        result.add((x, y+3))

    if is_diagonal(board) != False:

        pos_or_neg, x, y = is_diagonal(board)

        if pos_or_neg == "positiva":

            result.add((x, y))
            result.add((x+3,y+3))

        if pos_or_neg == "negativa":

            result.add((x, y))
            result.add((x-3, y+3))

    return result
