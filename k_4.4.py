from collections import deque #Подключениее библиотеки
n,k= map(int,input().split()) # присваивание переменных
nums=list(map(int,input().split())) # разделение данных чисел
deq=deque() # создание очереди
#5-9 поиск минимального элемента первого окна размером K
for i in range(k):
  while deq and nums[i] <nums[deq[-1]]: #поиск наименьшего элемента
    deq.pop() #удаление правого
  deq.append(i) #добавление i-го элемента
print(nums[deq[0]]) #Вывод минимального числа 1-го окна
for i in range(k,n): #цикл для остальных окон (n-k+1 условие выполняется )
  while deq and deq[0] <=i-k: #условме чтобы освободиться от элементов слева
    deq.popleft() #удаление левого элемента
  while deq and nums[i] <= nums[deq[-1]]: #поиск минимального
    deq.pop() #удаление правого
  deq.append(i) #добавление i-го элемента
  print(nums[deq[0]]) #вывод на экран