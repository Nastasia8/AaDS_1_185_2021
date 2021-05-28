n=int(input())
s=list(map(int, input (). split()))
stack=[]
t= True
num=1
for i in s:
    for _ in range (len(stack)):
        if stack and num == stack[-1]:
            stack.pop()
            num+=1
    if i!=num:
        if stack and i>stack[-1]:
            t= False
            break
        stack.append(i)
    else:
        num+=1
if t:
    print ("YES")
else:
    print ("NO")