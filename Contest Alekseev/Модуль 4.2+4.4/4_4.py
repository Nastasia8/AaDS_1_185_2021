n, k = map(int, input().split())
nums = list(map(int, input().split()))
stack = []
res = [0] * n
for i in range(n):
    while stack and nums[i] < nums[stack[-1]]:
        res[stack.pop()] = i
    stack.append(i)
while stack:
    res[stack.pop()] = n
i_n = 0
for i in range(n - k + 1):
    if i_n < i:
        i_n = i
    while res[i_n] < i + k:
        i_n = res[i_n]
    print(nums[i_n])