s = input()
stack = []
k = 0
for item in s:
    if item == '(':
        stack.append(item)
    elif item == ')':
        if stack:
            stack.pop()
        else:
            k += 1
print(k+len(stack))
