n = int(input())
numbers = []
for i in range(n):
    t = input().split()
    numbers.append(t)
numbers = [[int(numbers[i][j]) for j in range(2)] for i in range(n)]
for i in range(n-1):
    for j in range(n-1):
        if numbers[j][1] < numbers[j+1][1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
        if (numbers[j][1] == numbers[j+1][1]) and (numbers[j][0] > numbers[j+1][0]):
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
for i in range(n):
    print(" ".join(map(str, numbers[i])))
