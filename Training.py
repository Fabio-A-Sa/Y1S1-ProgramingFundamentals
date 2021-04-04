solution = []
def tourney(inp):
    
    solution.append(inp)
    if len(inp) == 2:
        solution.append([max(inp)])
        ret = []
        for item in solution:
            if item not in ret:
                ret.append(item)
        return ret

    else:
        sol = []
        while (len(inp)):
            sol.append(max(inp[:2]))
            inp = inp[2:]
        return tourney(sol)

print(tourney([9, 5, 4, 7, 6, 3, 8]))