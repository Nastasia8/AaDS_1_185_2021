n = int(input())
arr = input().split()[:n]
arr = [int(arr[i]) for i in range(n)]
k = 1
j = 0
while k != 0:
    k = 0
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            k += 1
            j += 1
            [print(item, end=' ') for item in arr]
            print('')
    if j == 0:
        print(0)