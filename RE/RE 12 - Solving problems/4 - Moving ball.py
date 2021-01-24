# Created on January, 2021
# @author: Fábio Araújo de Sá

def partida(board):

    cardinal = ["N", "S", "E", "O"]

    # Search in matriz
    for x, y in enumerate(board):
        for z, c in enumerate(y):
            if c in cardinal:

                ponto = (x, z)
                sentido_inicial = c

                return ponto, sentido_inicial

def new_direction(coordinate, objecto):

    if objecto == "\\" and (coordinate == "E" or coordinate == "S"):
        c = ["E", "S"]
        return c[c.index(coordinate)-1]

    if objecto == "\\" and (coordinate == "O" or coordinate == "N"):
        c = ["O", "N"]
        return c[c.index(coordinate)-1]

    if objecto == "/" and (coordinate == "E" or coordinate == "N"):
        c = ["E", "N"]
        return c[c.index(coordinate)-1]

    if objecto == "/" and (coordinate == "O" or coordinate == "S"):
        c = ["O", "S"]
        return c[c.index(coordinate)-1]

    return coordinate

def move_ball(board):

    coordinates = []

    directions = {
        "N" : (0, -1),
        "S" : (0, +1),
        "E" : (+1, 0),
        "O" : (-1, 0),
    }

    begin = partida(board)
    final = "X"
    coordinates.append(begin[0])

    x = begin[0][0]
    y = begin[0][1]
    rumo = begin[1]

    while final not in board[x][y]:

        sentido = directions[rumo]
        x = x + sentido[1]
        y = y + sentido[0]
        coordinates.append((x, y))
        rumo = new_direction(rumo, board[x][y])

    return coordinates
