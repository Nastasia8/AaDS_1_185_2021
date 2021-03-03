def function(n):
    if n==0:
        return 0
    if n==1:
        return 2
    if n==2:
        return 5
    return function(n-1) + function(n-2) + function(n-3)

for i in range(0,16):
    print(function(i), end=" ")