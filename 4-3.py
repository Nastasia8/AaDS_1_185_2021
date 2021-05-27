n=int(input())
nums=list(map(int,input().split()))#ввод чисел
stack=[]
index=[0]*n#создание списка нулей размера Н
d={i:nums[i] for i in range(n)}#
for i in range(n-1,-1,-1):#идем по циклу в обратном направлении
    while stack and stack[-1][1]>=d[i]:#если есть стек и число справа меньше текущего
        stack.pop()
    if not stack:#если нет стека то присваиваем элементу -1
        index[i]=-1
    else:
        index[i]=stack[-1][0]
    stack.append([i,d[i]])#добавляем элемент в стек
print(*index)#вывод списка