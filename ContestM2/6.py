

n = int(input())
list_c = input().split()
list_c = [int(list_c[i]) for i in range(n)]

k = int(input())
list_p = input().split()
list_p = [int(list_p[i]) for i in range(k)]

[print("yes") if list_c[i] < list_p.count(i+1) else print("no") for i in range(0, n)]