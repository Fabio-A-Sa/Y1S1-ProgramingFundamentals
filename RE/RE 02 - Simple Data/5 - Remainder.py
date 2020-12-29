# Created on October, 2020
# @author: Fábio Araújo de Sá

import datetime
now = datetime.datetime.now()
h = int(now.hour)
m = int(now.minute)

if h < 16:
    if m < 30:
        hh = h+8
        mm = m+30
    else:
        hh = h+9
        mm = m-30
        
else:
    if m < 30:
        hh = h+8-24
        mm = m+30
    else:
        hh = h+9-24
        mm = m-30
      
    
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
