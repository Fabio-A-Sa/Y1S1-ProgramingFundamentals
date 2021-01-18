def possibilities(board, player):

    def which_is(board, player):

        diagonal_1 = list([board[0][0], board[1][1], board[2][2]])
        diagonal_2 = list([board[0][2], board[1][1], board[2][0]])

        coluna_1 = list([board[0][0], board[1][0], board[2][0]])
        coluna_2 = list([board[0][1], board[1][1], board[2][1]])
        coluna_3 = list([board[0][2], board[1][2], board[2][2]])

        linha_1 = list(board[0])
        linha_2 = list(board[1])
        linha_3 = list(board[2])

        all_possibilities = list([diagonal_1, diagonal_2, coluna_1, coluna_2, coluna_3, linha_1, linha_2, linha_3])
        not_player = "x" if player == "o" else "o"

        for item in all_possibilities:
            if item.count(player) == 2 and not_player not in item:
                break

        return all_possibilities, item

    def coordenadas(atuple):

        letra = 0
        posição = 0

        all_possibilities = atuple[0]
        item = atuple[1]

        if item == all_possibilities[0]:
            # Diagonal 1
            local = item.index(" ")
            return local, local

        if item == all_possibilities[1]:
            # Diagonal 2
            local = item.index(" ")
            return 2-local, local
        
        colunas = list([all_possibilities[2], all_possibilities[3], all_possibilities[4]])
        if item in colunas:
            n = list([colunas[i] for i in range(3) if colunas[i] == item])
            posição = colunas.index(item)
            letra = n[0].index(" ")
            return letra, posição

        linhas = list([all_possibilities[5], all_possibilities[6], all_possibilities[7]])
        if item in linhas:
            n = list([linhas[i] for i in range(3) if linhas[i] == item])
            posição = n[0].index(" ")
            letra = linhas.index(item)
            return letra, posição
    
    return coordenadas(which_is(board, player))

def string_to_matrix(astring):

    alist = [[], [], []]

    i = 0
    for item in astring.split("\n"):
        for substring in item:
            alist[i].append(substring)
        i = i + 1

    return alist

def tic_tac_toe(board, player):

    game = string_to_matrix(board)
    jogada_correcta = possibilities(game, player)

    (letra, posição) = jogada_correcta

    from string import ascii_uppercase as abc
    l = abc[letra]
    i = posição + 1

    return "{}{}".format(l, i)
