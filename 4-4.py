from collections import deque#подключаем модуль 2х сторонний список
n,k= map(int,input().split())#ввод 2х чисел
nums=list(map(int,input().split()))#ввод списка чисел
deq=deque()#создание 2х стороннего списка
for i in range(k):#в цикле, пока текущий элемент меньше последнего элемента 2го списка
  while deq and nums[i] <nums[deq[-1]]:
    deq.pop()#удаление последнего элемента
  deq.append(i)#добавляем текущий элемент
print(nums[deq[0]])#вывод 
for i in range(k,n):#для И от размера окна до конца
  while deq and deq[0] <=i-k:#пока первый элемент 2х связного списка меньше или равен i минус количество элементов в окне
    deq.popleft()# удалить левый элемент
  while deq and nums[i] <= nums[deq[-1]]:#пока текущий элемент меньше элемента с интексом последнего элемента 2х связного списка
    deq.pop()
  deq.append(i)
  print(nums[deq[0]])#выводим элемент с индексом списка с индексом 0