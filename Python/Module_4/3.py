n = int(input())
num = list(map(int, input().split()))[:n]
stack = []
indexes = [0]*n
for i in range(n-1, -1, -1):
    while stack and num[stack[-1]] >= num[i]:
        stack.pop()
    indexes[i] = stack[-1] if stack else -1
    stack.append(i)

[print(item) for item in indexes]
