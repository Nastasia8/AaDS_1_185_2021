from math import factorial
n = int(input())    
sum_ = 0
for k in range(1, n+1):
    sum_ += (-1)*k*((5-k)/factorial(k))
print(sum_)