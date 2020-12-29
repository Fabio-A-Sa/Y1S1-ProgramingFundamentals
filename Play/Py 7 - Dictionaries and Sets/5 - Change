# Created on December, 2020
# @author: Fábio Araújo de Sá

def change(money):
    
    porquinho_mealheiro = {2.0: 0, 1.0: 0, 0.5: 0, 0.2: 0, 0.1: 0, 0.05: 0, 0.02: 0, 0.01: 0}
    
    for dinheiro, quantidade in porquinho_mealheiro.items():
        
        porquinho_mealheiro[dinheiro] = quantidade + money//dinheiro
        money = round(money%dinheiro, 2)
    
    return porquinho_mealheiro
