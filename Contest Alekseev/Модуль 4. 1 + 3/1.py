def psp(S):
    stack = []
    k = 0
    for i in range(len(S)):
        if (S[i] == '('):
            stack.append(S[i])
        elif (stack != []) and (stack[len(stack) - 1] == '('):
            stack.pop()
        else:
            k += 1
    return k + len(stack)

S = input()
print(psp(S))