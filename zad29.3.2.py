s=input().replace(" ","")
stack=[]
for i in s:
    if i.isdigit():
        stack.append(int(i))
    else:
        s2=stack.pop()
        s1=stack.pop()
        if i=="+":
            stack.append(s1+s2)
        elif i=="*":
            stack.append(s1*s2) 
        else:
            stack.append(s1-s2)
print(stack[-1])