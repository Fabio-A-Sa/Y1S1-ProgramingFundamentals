# Created on April, 2021
# @author: Fábio Araújo de Sá

def normalization (alist):
    
    normal = []
    for item in alist:
        if type(item) != list:
            normal.append(item)
            
        else:
            normal = normal + normalization(item)
            
    return normal

def interleave(alist1, alist2):

    alist1 = normalization(alist1)
    alist2 = normalization(alist2)

    solution = []
    for index in range (min(len(alist1), len(alist2))):
        solution.append(alist1[index])
        solution.append(alist2[index])

    return solution

attemps =   [   [[1, [4, 2]], [3, [7, 4]]],     [['a', 'b', 'c'], [1, 2, 3]], 
                [[1, ['a', 'b'], 2], [3,    [True, False], 4]], 
                [[['1'], ['0', '1']],   [['a'],['b', 'c']]],   [[], []]        ]

for attemp in attemps:
    one = attemp[0]
    two = attemp[1]
    print(interleave(one, two))