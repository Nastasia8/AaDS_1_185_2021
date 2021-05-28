'''
n = int(input()) 
num = list(map(int, input().split()))[:n] 
stack = [] 
indexes = [0]*n 
for i in range(n-1, -1, -1):
    while stack and num[stack[-1]] >= num[i]: 
        stack.pop() 
    indexes[i] = stack[-1] if stack else -1 
    stack.append(i) #добавление i-го элемента в стек

print(*indexes) 
''' 
1-2 строки ввод данных
3-4 создание стека и списка
5 обратный цикл от 9 до 0
6 минимальное справа налево, если стек не пуст
7 удаление последнего в стеке
8если стек не пуст, то индекс= последний элемент
9
добавление елемента в стек
10 вывод
'''
def prefix(s):
    v = [0]*len(s)
    count = 1
    for i in range(1,len(s)):
        k = v[i-1]
        while k > 0 and s[k] != s[i]:
            k = v[k-1]
        if s[k] == s[i]:
            k = k + 1
        else:
            k = 0
        v[i] = k
        if v[i] < 2:
            count = i
    return count
s = input()
print(prefix(s))
