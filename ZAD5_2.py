n = int(input())
numbers = list(map(int, input().split()))[:n]
set_ = set(numbers)
print(len(set_))