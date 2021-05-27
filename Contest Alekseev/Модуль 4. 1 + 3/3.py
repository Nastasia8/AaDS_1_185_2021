n = int(input())
nums = list(map(int, input().split()))[:n]
stack = []
index = [0] * n
for i in range(n-1, -1, -1):
    while stack and nums[stack[-1]]>=nums[i]:
        stack.pop()
    index[i] = stack[-1] if stack else -1
    stack.append(i)
print(*index)