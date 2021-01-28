# Created on January, 2021
# @author: Fábio Araújo de Sá

def interleave(f1, f2):

    result = ""

    with open(f1, "r") as file_1:
        with open(f2, "r") as file_2:
            
            lines_f1 = list([line for line in file_1])
            lines_f2 = list([line for line in file_2])

            for l1 in lines_f1:
                for l2 in lines_f2:

                    if lines_f1.index(l1) == lines_f2.index(l2):
                        result = result + l1 + l2
    
    return result
