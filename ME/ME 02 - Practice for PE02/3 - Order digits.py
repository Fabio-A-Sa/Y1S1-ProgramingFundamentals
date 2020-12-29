# Created on November, 2020
# @author: Fábio Araújo de Sá

def order_digits(n):
    
    n = list(str(n))
    alist = []
    result = ()
    
    for i in range(len(n)):
        alist.append(int(max(n)))
        n.remove(max(n))
    
    sorted(alist, reverse=True)
    
    for item in alist:
        result = result + (item,)
    
    return result

# n = 9013322
# print(order_digits(n))
