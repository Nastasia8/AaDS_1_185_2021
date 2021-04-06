stack = list(input())
k = 0
if len(stack) > 1e5:
    sys.exit()
while stack:
    if stack[0] == '(':
        if (len(stack) != 1) and (stack[1] == ")"):
            stack.pop(0); stack.pop(0)
        else:
            k += 1
            stack.pop(0)
    else:
        stack.pop(0)
        k += 1
print(k)
#Вердикт - WA(Неверный ответ)
#Примеры ввода из задания и мною написанные варианты решает верно