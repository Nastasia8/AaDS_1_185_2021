n=int(input())
s=list(map(int, input (). split (maxsplit=n)))
stack=[]
isPsk= True
num=1
for i in s:
    for _ in range (len(stack)):
        if stack and num == stack[-1]:
            stack.pop()
            num+=1
    if i!=num:
        if stack and i>stack[-1]:
            isPsk= False
            break
        stack.append(i)
    else:
        num+=1
if isPsk==True:
    print ("YES")
else:
    print ("NO")