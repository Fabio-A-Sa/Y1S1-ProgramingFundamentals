# Created on October, 2020
# @author: Fábio Araújo de Sá

def ajustes(blist):
    
    for q in range (0, len(blist)):
        blist[q] = blist[q].lower() # all in lower case
        blist[q] = blist[q].replace(" ", "") # delete space between words
        
    for s in range (0, len(blist)):
        
        word = ''.join(sorted(blist[s]))
        blist[s] = word # ordem alfabética
        
    return blist


def ordem(answer):
    return answer[0].lower()
    

def anagrams(alist):

    answer = []
    blist = alist.copy()
    ajustes(blist)
    filtro = []
    
    for i in range (len(blist)):
        
        temporário = []
        
        if alist[i] in filtro:
            continue
        else:
            temporário.append(alist[i])
            
        for j in range (i+1, len(blist)):
            
            if blist[i] == blist[j] and (alist[j] not in answer):
                temporário.append(alist[j])
                filtro.append(alist[j])
                temporário = sorted(temporário)
                
        answer.append(temporário)
        
    return sorted(answer, key=ordem)
