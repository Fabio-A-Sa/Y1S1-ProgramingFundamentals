def race(v1, v2, g):
    
    from math import floor
    if v2 <= v1:
        return None

    else:

        time = floor((g / (v2-v1))*60*60)
        hours = time // (60*60)
        time = time - hours*60*60
        minutes = time // 60
        time = time - minutes*60
        seconds = time
        return [hours, minutes, seconds]

print(race(720, 850, 70))