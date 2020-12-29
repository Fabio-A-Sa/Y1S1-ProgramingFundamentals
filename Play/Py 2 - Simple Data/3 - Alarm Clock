# Created on October, 2020
# @author: Fábio Araújo de Sá

h = int(input())
m = int(input())

if h < 18:
    if m < 9:
        hh = h+6
        mm = m+51
    else:
        hh = h+7
        mm = m-9
        
else:
    if m < 9:
        hh = h+6-24
        mm = m+51
    else:
        hh = h+7-24
        mm = m-9


hhh = str(hh)
mmm = str(mm)

if mm < 10:
    if hh < 10:
        print("0" + hhh + ":0" + mmm)
    else:
        print(hhh + ":0" + mmm)
else:
    if hh < 10:
        print("0" + hhh + ":" + mmm)
    else:
        print(hhh + ":" + mmm)
