def qual_o_preço_desta_montra_final_haaaaaa(money, products, wishlist):

    total = 0 
    for coisa in wishlist:
        quantidade = wishlist[coisa]
        preço = products[coisa]
        total = total + quantidade * preço
        
    return tuple((total, False)) if total > money else tuple((total, True))

def normalization(alist):

    standardized = []

    for adict in alist:
        dictio = adict.copy()
        for key in dictio:
            if adict[key] == 0:
                del dictio[key]
        standardized.append(dictio)

    return standardized

def knapsack(money, products, wishlist):

    all_possibilities = []
    best_combination = 0
    best_solution = {}

    if (qual_o_preço_desta_montra_final_haaaaaa(money, products, wishlist))[1]:
        return wishlist # Found one possible solution
    
    # Rearranging
    else:
        for item in wishlist:
            solution = wishlist.copy()

            if wishlist.get(item) != 0:

                if solution[item] == 1:
                    del solution[item] # solution[item] - 1 == 0

                elif products.get(item) > money:
                    del solution[item] # Can't buy them

                else:
                    solution[item] = solution[item] - 1 # Can't buy them all
                
                possibility = qual_o_preço_desta_montra_final_haaaaaa(money, products, solution)

                if possibility[1] == True:
                    if possibility[0] > best_combination:

                        best_combination = possibility[0]
                        best_solution = solution
                        all_possibilities.append(best_solution)
                else:
                    other_possibility = knapsack(money, products, solution)
                    if type(other_possibility) is dict:
                        other_sum = qual_o_preço_desta_montra_final_haaaaaa(money, products, other_possibility)
                        if other_sum[1] == True:
                            if other_sum[0] > best_combination:

                                best_combination = other_sum[0]
                                best_solution = other_possibility
                                all_possibilities.append(best_solution)

    return (normalization(all_possibilities))[-1]
