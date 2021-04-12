# Created on April, 2021
# @author: Fábio Araújo de Sá

def diff(lst):

    solution = []

    for index in range(len(lst)-1):
        difference = lst[index] - lst[index + 1]
        solution.append(difference)
        
    return tuple(solution)

attemps = [[1, 4, 3], [1, 2, 10, 1], [5, 0, 7, 0, 2, 2, 1, 1, 5, 1], [3]]
for attemp in attemps:
    print(diff(attemp))