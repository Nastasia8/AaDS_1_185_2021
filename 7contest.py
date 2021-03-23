n = int(input())
k, p = 0, 1
k_max = 0
arr = []
for i in range(n):
    k = 0  
    x = int(input())
    arr.append(x)
    if x == 0:
        k = 1
    while x != 0:
        x = x//10
        k += 1
    if k > k_max:
        k_max = k
print('Initial array:')
for i in range(n):  
    k = 0
    m = arr[i]
    if arr[i] == 0:
        k = 1
    while m != 0:
        m = m//10
        k += 1
    arr[i] = f'{arr[i]}'
    for j in range(k_max-k):
        arr[i] = f'0{arr[i]}'
for i in range(n):
    if i == n-1:
        print(arr[i])
    else:
        print(str(arr[i])+', ', end="")
print('**********')
arr2 = [[] for i in range(10)]
for i in range(k_max-1, -1, -1):  
    print('Phase '+str(p))
    p += 1
    for j in range(n):
        for f in range(10):
            if arr[j][i] == str(f):
                arr2[f].append(arr[j])
    for l in range(10):
        if arr2[l] != []:
            print('Bucket ' +str(l)+': ', end="")
            for x in range(len(arr2[l])):
                if x != len(arr2[l])-1:
                    print(f'{arr2[l][x]}, ', end="")
                else:
                    print(arr2[l][x])
        else:
            print('Bucket '+str(l)+': empty')
    print('**********')
    arr.clear()
    for i in range(10):  
        while arr2[i] != []:
            arr.append(arr2[i].pop(0))

print("Sorted array:")
print(*arr,sep=", ")
