

def ss(i, k, num, indexes, stack, x=0):

    if indexes[i] - i >= k or indexes[i] == -1:
        return x
    else:
        x = num[indexes[i]]
        k -= indexes[i] - i
        i += 1
        return ss(i, k, num, indexes, stack, x)


n, k = map(int, input().split())
num = list(map(int, input().split()))[:n]
stack = []
indexes = [0]*n

for i in range(n-1, -1, -1):

    while stack and num[stack[-1]] >= num[i]:
        stack.pop()
    indexes[i] = stack[-1] if stack else -1
    stack.append(i)

for i in range(n):
    if indexes[i] == -1:
        print(num[i])
    elif indexes[i] - i >= k:
        print(num[i])
    elif indexes[i] - i == k-1:
        print(num[indexes[i]])
    else:
        print(ss(i, k, num, indexes, stack))
    if n - k == i:
        break
