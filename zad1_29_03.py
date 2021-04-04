s=input()
stack=[]
isPsp=True
for i in s:
    if i==")":
        if not stack or stack [-1]!="(":
            isPsp=False
            break
        stack.pop()
    elif i=="]":
        if not stack or stack [-1]!="[":
            isPsp=False
            break
        stack.pop()
    elif i=="}":
        if not stack or stack [-1]!="{":
            isPsp=False
            break
        stack.pop()
    else:
        stack.append(i)
if isPsp and not stack:
    print("Yes")
else:
    print("No")