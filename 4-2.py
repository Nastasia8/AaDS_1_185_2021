n=int(input())
s=list(map(int, input (). split()))#ввод списка чисел
stack=[]
t= True# Т присваивается истна
num=1
for i in s:#для И в списке С
    for _ in range (len(stack)):
        if stack and num == stack[-1]:#если есть стек и число равно последнему со стека, то удаляем и прибавляем 1 к числу
            stack.pop()
            num+=1
    if i!=num:#если И не равно номеру, то проверяем условие, если есть стек, И больше последнего элемента стека
        if stack and i>stack[-1]:
            t= False#присваиваем т ложь, затем завершаем поиск и добавляем И на стек
            break
        stack.append(i)
    else:
        num+=1
if t:# если Т ложь, то вывод ДА
    print ("YES")
else:
    print ("NO")