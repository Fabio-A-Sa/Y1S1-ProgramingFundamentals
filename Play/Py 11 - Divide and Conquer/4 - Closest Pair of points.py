  
# Created on January, 2021
# @author: Fábio Araújo de Sá

def ordenação(alist):
    return sorted(alist, key = lambda x: x[0])

def distâncias(ponto1, ponto2):

    from math import sqrt as raiz
    x1 = ponto1[0]
    x2 = ponto2[0]
    y1 = ponto1[1]
    y2 = ponto2[1]

    distance = round(raiz((x1 - x2)**2 + (y1 - y2)**2))
    return distance

def separação(alist):

    middle = len(alist)//2

    left = alist[:middle]
    right = alist[middle:]

    return (left, right)

def closest_pair(points):

    # Initial conditions
    if len(points) == 2:
        return distâncias(points[1], points[0])
    if len(points) == 3:
        return min( distâncias(points[0], points[1]), 
                    distâncias(points[0], points[2]), 
                    distâncias(points[1], points[2]))

    points = ordenação(points)

    left = separação(points)[0]
    right = separação(points)[1]

    min_distance = min(closest_pair(left), closest_pair(right))

    all_values = list([min_distance]) + list([distâncias(l, r) for l in left for r in right if abs(r[0]-l[0]) < min_distance])
    answer = min(all_values)

    return answer
