n = int(input())
num = list(map(int, input().split()))
stack = []
k = 1
T = True
for i in num:
    for j in range(len(stack)):
        if stack and k == stack[-1]:
            stack.pop()
            k += 1
        if i != k:
            if stack and i>stack[-1]:
                    T= False
                    break
            stack.append(i)
        else:
            k += 1
if T:
    print ("YES")
else:
    print ("NO")