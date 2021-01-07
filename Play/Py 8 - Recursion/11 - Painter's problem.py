# Created on December, 2020
# @author: Fábio Araújo de Sá

def poss(n, boards):

    # All possibilities to paint all boards
    qtd = len(boards) + 2 - n
    all_possibilities = []
    for x in range(1, qtd):
        possibility = paint(n-1, boards[x:]) + max(boards[:x])
        all_possibilities.append(possibility)
    
    return all_possibilities

def paint(n, boards):

    if n == 1:
        return max(boards)
    else:
        return min(poss(n, boards))
