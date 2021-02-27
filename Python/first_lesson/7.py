arr = [[1, 2, 3], [2, 2, 2], [2, 8, 3]]
def fuc(arr):
    k=2
    for i in arr:
        i[k] = i[k]*2
        k -= 1
    return arr
arr = fuc(arr)    
print(arr)