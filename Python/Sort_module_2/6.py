n = int(input())
numbers = list(map(int, input().split()))[:n]
k = int(input())
kumbers = list(map(int, input().split()))[:k]
sl = {key: 0 for key in range(1, n+1)}
for item in kumbers:
    for key in sl:
        if item == key:
            sl[key] += 1
for i in range(len(numbers)):
    if numbers[i] < sl[i+1]:
        print('yes')
    else:
        print('no')
