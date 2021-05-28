def shift_up(indx, heap):#К стандартному параметру добавляем входной параметр (индекс)
    while heap[indx] > heap[(indx-1)//2] and (indx-1)//2 >= 0:
        heap[indx], heap[(indx-1)//2] = heap[(indx-1)//2], heap[indx]
        indx = (indx-1)//2
# 2-3 алгоритм из коробки
    return indx+1 #возвращаем индекс

def shift_down(indx, heap):#К стандартному параметру добавляем входной параметр (индекс)
    while 2*indx+1 < len(heap):
        left_indx = 2*indx+1
        right_indx = 2*indx+2
        _indx = left_indx
        if right_indx < len(heap) and heap[left_indx] < heap[right_indx]:
            _indx = right_indx
        if heap[_indx] <= heap[indx]:
            break
        heap[indx], heap[_indx] = heap[_indx], heap[indx]
        indx = _indx #9-17 стандарт
    return indx+1 #возвращаем индекс

def add(item, heap):
    heap.append(item)
    return shift_up(len(heap)-1, heap) #все по 21-23 шаблону с добавлением индекса в параметры

def extract(heap):
    heap[0], heap[len(heap)-1] = heap[len(heap)-1], heap[0]
    value = heap.pop()
    if heap:
        return [shift_down(0, heap), value]
    else:
        return [0, value] # Возвращаем 0 , если удалили последний элемент и его значение

def get_max(heap):
    return heap[0]

def main():
    info=list(map(int,input().split())) #37-38,42 вводим данные
    n,m=info[:2]
    heap = [] # 39-40 готовим почву 
    res = []
    for _ in range(m):
        command = list(map(int,input().split()))
        if command[0] == 1:
            if not heap: # Если дерево пустое выводим -1
                res.append(-1)
            else: #Иначе добавляем значение индекса и значения в результат 
                res.append(extract(heap))
        elif command[0]==2:
            if len(heap) == n: # проверка на количество запросов, если больше то -1
                res.append(-1)
            else:
                res.append(add(command[-1], heap)) # добавляем в кучу,добавляем в результат индекс и значение нового элемента
    [print(i) if type(i)==int else print(*i) for i in res],print(*heap) # красивый вывод
    

main()