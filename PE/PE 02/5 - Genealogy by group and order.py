# Created on December, 2020
# @author: Fábio Araújo de Sá

def genealogy(l1):
    
    pat_sibling = [] # colocar os nomes "iguais"
    pat_parent = []
    pat_cousin = []
    pat_grandparent = []
    total = []
    
    
    for i in range(len(l1)):
        
        if l1[i][1] == "sibling":
            pat_sibling.append(l1[i][0])
            
        elif l1[i][1] == "parent":
            pat_parent.append(l1[i][0])
            
        elif l1[i][1] == "cousin":
            pat_cousin.append(l1[i][0])
            
        elif l1[i][1] == "grandparent":
            pat_grandparent.append(l1[i][0])
            
    
    answer1 = (sorted(pat_sibling), "sibling")
    answer2 = (sorted(pat_parent), "parent")
    answer3 = (sorted(pat_cousin), "cousin")
    answer4 = (sorted(pat_grandparent), "grandparent")
    
    total.append(answer1)
    total.append(answer2)
    total.append(answer3)
    total.append(answer4)
    
#    for j in range(len(total)):
#        if total[j][0] == []:
#            total.remove(total[j])

    for item in total:
        
        if item == ([], "sibling"):
            total.remove(item)
        elif item == ([], "parent"):
            total.remove(item)
        elif item == ([], "cousin"):
            total.remove(item)
        elif item == ([], "grandparent"):
            total.remove(item)

    for item in total:
        
        if item == ([], "sibling"):
            total.remove(item)
        elif item == ([], "parent"):
            total.remove(item)
        elif item == ([], "cousin"):
            total.remove(item)
        elif item == ([], "grandparent"):
            total.remove(item)
        
        
    return total
