import random
from pprint import pprint

def izm(arr, m):
    for i in range(m):
        arr[i][m-1-i] *= 2
    return arr

m = 5
arr = [[random.randint(0,20) for i in range(m)] for j in range(m)]
pprint(arr)
print()
pprint(izm(arr, m))