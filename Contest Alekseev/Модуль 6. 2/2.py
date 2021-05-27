def shift_up(indx, heap): #добавляем первый индекс
    while heap[indx] > heap[(indx-1)//2] and (indx-1)//2 >= 0:
        heap[indx], heap[(indx-1)//2] = heap[(indx-1)//2], heap[indx]
        indx = (indx-1)//2

    return indx+1 #возвращаем индекс

def shift_down(indx, heap): #также добавляем первый индекс
    while 2*indx+1 < len(heap): #пока дочерний индекс меньше длины кучи (индекс элемента не может быть больше длины кучи)
        left_indx = 2*indx+1 #определяем правый и левый индексы
        right_indx = 2*indx+2
        _indx = left_indx
        if right_indx < len(heap) and heap[left_indx] < heap[right_indx]: #первое условие (9) и куча[левый индекс] < куча[правый индекс]. Определяем для того, чтобы менять местами индкексы
            _indx = right_indx
        if heap[_indx] <= heap[indx]: #_indx - переменная для перемещения значений
            break
        heap[indx], heap[_indx] = heap[_indx], heap[indx]
        indx = _indx 
    return indx+1 

def add(item, heap):
    heap.append(item)
    return shift_up(len(heap)-1, heap) #добавление индекса по параметрам

def extract(heap):
    heap[0], heap[len(heap)-1] = heap[len(heap)-1], heap[0] #множественное переприсваивание
    value = heap.pop()
    if heap:
        return [shift_down(0, heap), value]
    else:
        return [0, value]

def extract_supper(indx,heap):
    value_last=heap[-1]
    heap[-1],heap[indx-1]=heap[indx-1],heap[-1]
    value_indx=heap.pop()
    if value_last <= value_indx:
        shift_down (indx-1,heap)
    else:
        shift_up(indx-1,heap)

    return value_indx



def get_max(heap):
    return heap[0]

def main():
    info=list(map(int,input().split())) 
    n,m=info[:2]
    heap = []
    res = []
    for _ in range(m):
        command = list(map(int,input().split()))
        if command[0] == 1:
            if not heap: #если куча пустая, то вывод -1, иначе добавляем значение индекса
                res.append(-1)
            else:
                res.append(extract(heap))
        elif command[0] == 2:
            if len(heap) == n:
                res.append(-1)
            else:
                res.append(add(command[1], heap))
        else:
            if len(heap) < command[1] or command[1]==0:
                res.append(-1)
            else:
                res.append(extract_supper(command[1], heap))


    [print(i) if type(i)==int else print(*i) for i in res],print(*heap) 

main() 