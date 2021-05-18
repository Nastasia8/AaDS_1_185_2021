n = int(input())
string = list(map(int, input().split()))
stack = []
isPsk = True
num = 1
for i in string:
    for j in range(len(stack)):
        if stack and num == stack[-1]:
            stack.pop()
            num += 1
    if i != num:
        if stack and i > stack[-1]:
            isPsk = False
            break
        stack.append(i)
    else:
        num += 1
if isPsk:
    print ("YES")
else:
    print ("NO")