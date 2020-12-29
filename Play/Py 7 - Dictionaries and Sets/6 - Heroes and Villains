# Created on December, 2020
# @author: Fábio Araújo de Sá

def fight(heroes, villain):
    
    # Escolha dos heróis para lutar
    heroes_that_fight = []
    for heroe in heroes:   
        if heroe['category'] == villain['category']:
            heroes_that_fight.append(heroe)
    #Luta
    bons_venceram = False
    for heroe in heroes_that_fight:
        
            if heroe["health"] < villain["health"]:
                villain["health"] = villain["health"] - round(((heroe["health"])/2), 2)
                bons_venceram = bons_venceram and False
            else:
                bons_venceram = bons_venceram or True
                break
            
    name_good = heroe["name"]
    score_good = heroe["score"] + 1
    good_wins = f"{name_good} defeated the villain and now has a score of {score_good}"
    bad_wins = villain['name'] + " prevailed with "+ str(villain["health"]) + "HP left"
    
    return good_wins if bons_venceram else bad_wins
