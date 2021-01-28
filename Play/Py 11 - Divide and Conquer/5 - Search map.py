  
# Created on January, 2021
# @author: Fábio Araújo de Sá

def search_map(amap, map_rectangle, search_rectangle):

    # Condição Base
    if amap is None:
        return set()
    
    if type(amap) == str:
        return set(amap)

    # Definir os mapas
    mapx = map_rectangle[0]
    mapy = map_rectangle[1]
    mapz = map_rectangle[2]
    mapt = map_rectangle[3]

    # Definir áreas procuradas
    x = search_rectangle[0]
    y = search_rectangle[1]
    z = search_rectangle[2]
    t = search_rectangle[3]

    answer = set() # Acumulador dos objectos

    if x <= mapx + mapz/2 and y <= mapy + mapt/2:
        # Se estiver no quadrante 1, chamada recursiva
        answer = answer | search_map(amap[0], (mapx, mapy, mapz/2, mapt/2), search_rectangle)

    if (x + z) >= mapx + mapz/2 and y <= mapy + mapt/2:
        # Se estiver no quadrante 2, chamada recursiva
        answer = answer | search_map(amap[1], (mapx + mapz/2, mapy, mapz/2, mapt/2), search_rectangle)

    if (x + z) >= mapx + z/2 and (y + t) >= mapy + mapt/2:
        # Se estiver no quadrante 3, chamada recursiva
        answer = answer | search_map(amap[2], (mapx + mapz/2, mapy + mapt/2, mapz/2, mapt/2), search_rectangle)

    if x <= mapx + mapz/2 and (y + t) >= mapy + mapt/2:
        # Se estiver no quadrante 4, chamada recursiva
        answer = answer | search_map(amap[3], (mapx, mapy + mapt/2, mapz/2, mapt/2), search_rectangle)

    return set(answer)
