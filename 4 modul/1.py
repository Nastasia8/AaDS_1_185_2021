string= input()
stack=[]
count=0
for i in string:
    if i==")":
        if not stack or stack [-1]!="(":
            count+=1
        if stack and stack [-1]=="(":
            stack.pop() 
    else:
        stack.append(i)

if stack:
    count+=len(stack)
print(count)