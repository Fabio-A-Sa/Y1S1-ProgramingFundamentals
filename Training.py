

def choose_best_sum(t, k, ls):
    
    from itertools import permutations 

    possible_attemps = list(permutations(ls, k))
    total_sum = [sum(alist) for alist in possible_attemps if int(sum(alist)) <= t]
    maximum = max(total_sum)
    return maximum if maximum <= t else None
    
ls = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
k = 4
t = 230
print(choose_best_sum(t, k, ls))