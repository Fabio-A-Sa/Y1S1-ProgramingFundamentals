# Created on December, 2020
# @author: Fábio Araújo de Sá

def evaluate(a, x):
    from functools import reduce as r
    expoentes = [e for e in range(len(a))]
    fatores = [n*(x**e) for n,e in zip(a,expoentes)]
    return r(lambda x,y: x+y, fatores)
