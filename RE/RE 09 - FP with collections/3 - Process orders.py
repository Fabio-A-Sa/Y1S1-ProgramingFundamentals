# Created on October, 2020
# @author: Fábio Araújo de Sá

def coisa(x, y, min):
    return (x*y if x*y>min else x*y+10)
    
def invoice_totals(orders, min):
    return [(item[0], coisa(item[2], item[3], min)) for item in orders]
