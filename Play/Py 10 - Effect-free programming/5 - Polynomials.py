# Created on January, 2021
# @author: Fábio Araújo de Sá

def evaluate(a, x):

    expoentes = [e for e in range(len(a))]
    fatores = [n*(x**e) for n,e in zip(a,expoentes)]

    return sum(fatores)
