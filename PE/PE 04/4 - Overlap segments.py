# Created on January, 2021
# @author: Fábio Araújo de Sá

def overlaps(segments):
    
    result = []
    
    for i in range(len(segments)):
        
        for j in range(i, len(segments)):
            
            if j > i:
                
                alist1 = [x for x in range(segments[i][0], segments[i][1])]
                alist2 = [x for x in range(segments[j][0], segments[j][1])]
                local_tuple = ()
                
                for number in alist2:
                    if number in alist1:
                        
                        # Interseção!
                        local_tuple = i, j
                        result.append(local_tuple)

    return set(result)
  
# JCL's better solution:

def is_overlap(s1, s2) -> bool:
    """ find out if the two segments (start, end) overlap """
    return not (s1[0] > s2[1] or s1[1] < s2[0])
    
def overlaps(segments):
    # using a set comprehension, compare each segment with all the others
    return {(i, j) for i in range(len(segments)) for j in range(i+1, len(segments)) if is_overlap(segments[i], segments[j])}
