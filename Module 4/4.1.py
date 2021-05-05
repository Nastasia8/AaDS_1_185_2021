s = input()
k = 0
stack = []
for i in s:
    if i==")":
        if stack:
            stack.pop()
            k+=2
    else:
        stack.append(i)
print(len(s) - k)