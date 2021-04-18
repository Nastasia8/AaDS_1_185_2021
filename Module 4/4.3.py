n = int(input())
array = list(map(int, input().split()))
stack = []
index = [0] * n
dictionary = {i: array[i] for i in range(n)}
for i in range(n - 1, -1, -1):
    while stack and stack[-1][1] >= dictionary[i]:
        stack.pop()
    if not stack:
        index[i] = -1
    else:
        index[i] = stack[-1][0]
    stack.append([i, dictionary[i]])
print(*index)