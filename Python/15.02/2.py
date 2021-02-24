import math
n = int(input('n = '))
k = 1
s = 0
for k in range(k, n):
    s += (-1)*k*((k-5)/math.factorial(k))
print(s)
