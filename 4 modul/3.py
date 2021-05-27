g = int(input())
nums = list(map(int,input().split()))[:g]
a = {i:nums[i] for i in range (g)}
stack = []
index = [0]*g
for i in range(g-1,-1,-1):
        while stack and stack[-1][1] >= a[i]:
            stack.pop()
        if not stack:
            index[i] = -1
        else:
            index[i] = stack[-1][0]
        stack.append([i, a[i]])
print(*index)