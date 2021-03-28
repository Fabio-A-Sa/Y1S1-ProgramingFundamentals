def isPP(n):
    
    from math import pow, sqrt
    solution = []

    for i in range (2, int(sqrt(n)+4)):
        for j in range(2, int(sqrt(n)+4)):

            if pow(i, j) == n:
                solution.append(i)
                solution.append(j)
                return solution

            if pow(i, j) > n:
                break
            
        else:
            continue

    return None

print(isPP(8))