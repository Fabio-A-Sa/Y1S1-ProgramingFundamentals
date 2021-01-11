# Created on January, 2021
# @author: Fábio Araújo de Sá

def bubble_sort(alist):

    s = len(alist)
    aux = 0

    if s == (0 or 1):
        return alist

    else:
        for x in range(s):

            counter = 0
            flag = True

            while counter + 1 < s :
                if alist[counter] > alist[counter+1]:
                    aux = alist[counter+1]
                    alist[counter+1] = alist[counter]
                    alist[counter] = aux
                    flag = flag and False
                counter = counter + 1

            if flag == True:
                # Not changed any more values
                return alist
