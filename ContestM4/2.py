

def func(list_):
    stack = []
    list_copy = list_.copy()
    for i in list_:
        stack.insert(0, i)
        if i == min(list_copy):
            list_copy.remove(i)
            stack.remove(i)
            for j in stack:
                if j == min(list_copy):
                    list_copy.remove(j)
                    stack.remove(j)
                else:
                    break
    if len(stack) == 1 and stack[0] == max(list_copy):
        stack.pop()
    if stack:
        print("NO")
    else:
        print("YES")
        

n = int(input())
list_ = input().split()
list_ = [int(list_[i]) for i in range(n)]
func(list_)
        

