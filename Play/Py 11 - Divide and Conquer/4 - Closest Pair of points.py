def ordem(something):
    # Coordenada x 
    return something[0]

def ordenação(alist):
    return sorted(alist, key=ordem)

def distâncias(ponto1, ponto2):

    from math import sqrt as raiz
    x1 = ponto1[0]
    x2 = ponto2[0]
    y1 = ponto1[1]
    y2 = ponto2[1]

    distance = round(raiz((x1 - x2)**2 + (y1 - y2)**2))
    return distance

def separação(alist):

    n = len(alist)
    if n%2 == 1:
        middle = (n-1)//2
    else:
        middle = n//2

    left = alist[:middle]
    right = alist[middle:]

    return (left, right)

def rec_distance(alist, best_distance = 10000000000000):

    

    return best_distance

def closest_pair(points):

    points = ordenação(points)
    
    left = separação(points)[0]
    right = separação(points)[1]

    min_distance_left = rec_distance(left)
    min_distance_right = rec_distance(right)

    return left, right

points = [(2498, 7397), (2168, 8117), (2168, 6677), (1496, 1976), (8893, 9240), (288, 9467), (7465, 8080), (4588, 1774), (4178, 8118), (3459, 7224)]
print(closest_pair(points))
