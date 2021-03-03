def prost(n):
    numbers = [i for i in range(1, n+1)]
    for i in numbers:
        for j in numbers:
            if (j != i) and (j % i == 0):
                numbers.remove(j)
    print(numbers)

n = int(input("n: "))
prost(n)