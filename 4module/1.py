s= input()
stack=[]
k=0
for i in s:
    if i==")":
        if not stack or stack [-1]!="(":
            k+=1
        if stack and stack [-1]=="(":
            stack.pop()   
    else:
        stack.append(i)

if stack:
    k+=len(stack)
print(k)