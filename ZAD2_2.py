def F(n):
    if n == 0:
        return 0
    if n == 1:
        return 3
    if n == 2:
        return 5
    if n > 2:
        return F(n-1) + F(n-2) + F(n-3)

n = 15
for i in range(n+1):
    print(F(i))