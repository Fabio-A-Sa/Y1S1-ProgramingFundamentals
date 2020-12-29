# Created on December, 2020
# @author: Fábio Araújo de Sá

def permutations(atuple):
    
    if len(atuple) == 0:
        pass

    if len(atuple) == 1:
        return set((atuple,))
    
    if len(atuple) == 2:
        new_tuple = ((atuple, (atuple[1], atuple[0])))
        return set(new_tuple)
    
    else: # 3 or more
        permutações = set()
        for idx in range(len(atuple)):
            for other_thing in permutations(atuple[:idx] + atuple[idx+1:]):
                permutações.add(((atuple[idx],) + other_thing))
                
    return permutações
    
# atuple = ('A', 'B', 'C')
# print(permutations(atuple))
