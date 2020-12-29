# Created on December, 2020
# @author: Fábio Araújo de Sá

def ajustes(budget, products, wishlist, preço_total):
  
    # Ordem da lista: valor menor --> valor maior
    preços_ordenados = sorted(products.items(), key = lambda a: a[1])
    
    # Nova combinação das compras
    comprados = wishlist.copy()
    for produto, valor in preços_ordenados:
        if produto in comprados.keys():
            
            while preço_total > budget and comprados[produto] > 0 and produto in wishlist:
                preço_total -= valor
                comprados[produto] += -1
                
            # Eliminar o produto do set quando este já não existe
            if comprados[produto] == 0:
                del comprados[produto]
                
    return comprados
    
def budgeting(budget, products, wishlist):
    
    preço_total = 0
    for produto, quantidade in wishlist.items():
        preço_total = preço_total + products[produto]*quantidade
    
    return wishlist if preço_total < budget else ajustes(budget, products, wishlist, preço_total)
