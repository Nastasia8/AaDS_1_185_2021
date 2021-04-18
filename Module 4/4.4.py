n, k = map(int, input().split())
lst = list(map(int, input().split()))
 
for i in range(n - k + 1):
    print(min(lst[i:i + k]))


#Work in progress