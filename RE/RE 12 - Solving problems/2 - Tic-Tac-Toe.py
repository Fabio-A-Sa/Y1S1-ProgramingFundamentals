def possibilities(board, player):

    def which_is(board, player):

        diagonal_1 = list([board[0][0], board[1][1], board[2][2]])
        diagonal_2 = list([board[0][2], board[1][1], board[2][0]])

        coluna_1 = list([board[0][0], board[0][1], board[0][2]])
        coluna_2 = list([board[1][0], board[1][1], board[1][2]])
        coluna_3 = list([board[2][0], board[2][1], board[2][2]])

        linha_1 = list(board[0])
        linha_2 = list(board[1])
        linha_3 = list(board[2])

        all_possibilities = (diagonal_1, diagonal_2, coluna_1, coluna_2, coluna_3, linha_1, linha_2, linha_3)
        not_player = "x" if player == "o" else "o"

        for item in all_possibilities:
            if item.count(player) == 2 and item.count(not_player) == 0:
                break

        return item
    
    return which_is(board, player)

def string_to_list(astring):

    alist = [[], [], []]

    i = 0
    for item in astring.split("\n"):
        for substring in item:
            alist[i].append(substring)
        i = i + 1

    return alist

def tic_tac_toe(board, player):

    game = string_to_list(board)
    jogada_correcta = possibilities(game, player)

    return jogada_correcta

board = 'x x\n o \nxoo'
player = "o"
print(tic_tac_toe(board, player))
