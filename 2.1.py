def fact(n):
    f = 1
    for i in range(1,n+1):
        f *= i
    print(f)

n = int(input("n = "))
fact(n)