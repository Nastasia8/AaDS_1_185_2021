s = input().replace(" ", "")
d = {"*":3, "/":3, "+":2, "-":2, "(":1}
stack = [] # [operation, prior]
s_res = []
def in_pos(s):
    stack = []
    for i in s:
        if i in "+-/*()":
            n2 = stack.pop()
            n1 = stack.pop()
            if i == "+":
                stack.append(n1 + n2)
            elif i == "-":
                stack.append(n1 - n2)
            elif i == "*":
                stack.append(n1 * n2)
            elif i == "/":
                stack.append(n1 // n2)
        else:
            stack.append(int(i))
    print(stack[-1])


for i in s:
    if i in "+-/*()":
        if i == ")":
            while stack[-1][0] != "(":
                s_res.append(stack.pop()[0])
            stack.pop()
            continue
        while stack and stack[-1][0] >= d[i] and i != "(":
            s_res.append(stack.pop()[0])
        if not stack or stack[-1][1] < d[i] and i == "(":
            stack.append([i, d[i]])
    else:
        s_res.append(i)
while stack:
    s_res.append(stack.pop()[0])

print(*s_res)
in_pos(s_res)