n = int(input())
numbers = list(input().split())
numbers.sort()

count = 1
for i in range(1, n):
    if numbers[i - 1] != numbers[i]:
        count += 1
print(count)