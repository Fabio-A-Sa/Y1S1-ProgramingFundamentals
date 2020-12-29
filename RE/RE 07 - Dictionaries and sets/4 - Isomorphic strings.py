# Created on October, 2020
# @author: Fábio Araújo de Sá

def same_size(astring1, astring2):
    return (len(astring1) == len(astring2))


def is_isomorphic(astring1, astring2):
    
    dict1 = {} # letras de astring 1
    dict2 = {} # letras de astring 2
    
    for i, value in enumerate(astring1):
        if value in dict1:
            
            if astring2[i] != dict1[value]:
                return False
        else:
            dict1[value] = astring2[i]
            
        if astring2[i] in dict2:
            
            if value != dict2[astring2[i]]:
                return False
        else:
            dict2[astring2[i]] = value
            
    return True


def isomorphic(astring1, astring2):
    
    alist = []
    blist = []
    letras_pares = ()
    pairs = []
    
    if same_size(astring1, astring2):
        
        for letter in astring1:
            alist.append(letter)
            
        for letter in astring2:
            blist.append(letter)
            
        for x in range(len(alist)):
            for y in range(len(blist)):
                if x == y:
                    letras_pares = (alist[x], blist[y])
                else:
                    continue
                
            if letras_pares not in pairs:
                pairs.append(letras_pares)
        
        resposta_verdadeira = f"'{astring1}' and '{astring2}' are isomorphic because we can map: {pairs}"
        resposta_falsa = f"'{astring1}' and '{astring2}' are not isomorphic"
        
        return resposta_verdadeira if is_isomorphic(astring1, astring2) else resposta_falsa
    
    return #None

# astring1 = 'turtle'
# astring2 = 'tletur'
# print(isomorphic(astring1, astring2))
