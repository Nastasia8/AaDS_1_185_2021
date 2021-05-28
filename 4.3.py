n = int(input()) 
num = list(map(int, input().split()))[:n] 
stack = [] 
indexes = [0]*n 
for i in range(n-1, -1, -1):
    while stack and num[stack[-1]] >= num[i]: 
        stack.pop() 
    indexes[i] = stack[-1] if stack else -1 
    stack.append(i) 

print(*indexes) 
''' 
1-2 строки ввод данных
3-4 создание стека и списка
5 обратный цикл от 9 до 0
6 минимальное справа налево, если стек не пуст
7 удаление последнего в стеке
8если стек не пуст, то индекс= последний элемент
9
добавление элемента в стек
10 вывод