h = [2,1,5,6,2,3]
n = len(h)
stack = []
l = [0]*n
r =[0]*n
for i in range(n):
    while stack and h[stack[-1]] >= h[i]:
        stack.pop()
    l[i] = stack[-1] if stack else -1
    stack.append(i)
stack.clear()

for i in range(n-1, -1, -1):
    while stack and h[stack[-1]] >= h[i]:
        stack.pop()
    r[i] = stack[-1] if stack else n
    stack.append(i)

res = 0
for i in range(n):
    res = max(res, h[i] * (r[i] - l[i] - 1))
print(res)