# Created on December, 2020
# @author: Fábio Araújo de Sá

def last_man_standing(alist, step, initial_idx=0):

    if len(alist) == 1:
        return alist[0]
    else:
        idx = (step-1+initial_idx)%(len(alist))
        alist.remove(alist[idx])
        return last_man_standing(alist, step, idx)
