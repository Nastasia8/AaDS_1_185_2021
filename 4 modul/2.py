n = int(input())
string = list(map(int, input().split()))
stack = []
isPsk = True
num = 1
for g in string:
    for j in range(len(stack)):
        if stack and num == stack[-1]:
            stack.pop()
            num += 1
    if g != num:
        if stack and g > stack[-1]:
            isPsk = False
            break
        stack.append(g)
    else:
        num += 1
if isPsk:
    print ("DA")
else:
    print ("NET")