# Created on January, 2021
# @author: Fábio Araújo de Sá

from difflib import unified_diff as df
# https://docs.python.org/3/library/difflib.html

def diff(filename1, filename2):

    file1 = open(filename1, 'r').readlines()
    one = list([" " + line for line in file1])
    file2 = open(filename2, 'r').readlines()
    two = list([" " + line for line in file2])

    difference = list(df(one, two, fromfile = "file1", tofile = "file2", lineterm=""))
    
    for line in difference:
        if line[0] == " ":
            difference.remove(line)

    acumulator = ""
    for line in difference:
        acumulator = acumulator + line

    return acumulator[33:]
