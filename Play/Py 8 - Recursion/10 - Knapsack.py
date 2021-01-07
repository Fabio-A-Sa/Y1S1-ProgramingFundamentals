# Created on December, 2020
# @author: Fábio Araújo de Sá

def não_falido(money, products, wishlist):

    gasto = 0
    for item in wishlist:
        quantidade = wishlist.get(item)
        preço = products.get(item)
        gasto = gasto + preço*quantidade

    return True if (gasto < money or money == gasto) else False

def knapsack(money, products, wishlist):

    all_possibilities = []

    if não_falido(money, products, wishlist):
        # Found the best solution
        return wishlist
    
    # Rearranging
    for item in wishlist:
        solution = wishlist.copy()
        if wishlist.get(item) != 0:
            if products.get(item) > money:
                # Can't buy them
                solution[item] = 0
            else:
                # Can't buy them all
                solution[item] = solution[item] - 1
            
            all_possibilities.append(solution)

    for possibility in all_possibilities:
        if não_falido(money, products, possibility):
            continue
        else:
            # Error
            for item in possibility:
                nova = knapsack(money, products, item)
                all_possibilities.append(nova)
    
    all_prices = []
    for possibility in all_possibilities:
        quantidade = wishlist.get(possibility)
        preço = products.get(possibility)
        gasto = gasto + preço*quantidade
        all_prices.append(gasto)

    final = {}
    for item, qtd in enumerate(all_possibilities.index(max(all_prices)).itens()):
        if qtd != 0:
            final = final + {item:qtd}

    return final
