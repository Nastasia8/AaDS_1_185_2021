#Shift_up,  shift_down стандартный код, только возвращаем индекс + 1
def shift_up(index, heap):  
    while heap[index] > heap[(index-1)//2] and (index-1)//2 >= 0:
        heap[index], heap[(index-1)//2] = heap[(index-1)//2], heap[index]
        index = (index-1)//2
    return index+1

def shift_down(index, heap):
    while 2*index+1 < len(heap):
        left_index = 2*index+1
        right_index = 2*index+2
        child_index = left_index
        if right_index < len(heap) and heap[left_index] < heap[right_index]:
            child_index = right_index
        if heap[child_index] <= heap[index]:
            break
        heap[index], heap[child_index] = heap[child_index], heap[index]
        index = child_index
    return index+1

def add(item, heap):
    heap.append(item)
    return shift_up(len(heap)-1, heap)

def direct_extract(index, heap): #функция удаления по индексу
    val = heap[len(heap)-1] #последний элемент
    heap[index-1], heap[len(heap)-1] = heap[len(heap)-1], heap[index-1] #меняет последний и первый по индексу элемент
    ind = heap.pop() #запоминаем элемент который удалили
    if val < ind: #Если последний меньше чем который удалили то опускаем, иначе поднимаем
        shift_down(index-1, heap)
    elif val > ind:
        shift_up(index-1, heap)
    return ind #возвращаем элемент который удалили
    
def extract(heap):
    heap[0], heap[len(heap)-1] = heap[len(heap)-1], heap[0]
    ind = heap.pop()
    if heap:
        return shift_down(0, heap), ind
    else:
        return 0, ind

def get_max(heap):
    return heap[0]

def main():
    heap = [] 
    result = []
    input_ = input().split() #считывание строки
    n, m = int(input_[0]), int(input_[1]) #разделение на переменные n и m
    for i in range(m): #цикл до m
        data = input().split() # считываем информацию
        if int(data[0]) == 1: #первая операция
            if not heap: #если пустая куча
                result.append(-1) # вывод -1 по условию
            else:
                result.append(extract(heap)) # иначе если не пустая, то удаляем максимальный 
        elif int(data[0]) == 2: # вторая операция
            if len(heap) == n: # размер кучи =  максимальному размеру
                result.append(-1) # вывод -1 по условию
            else:
                result.append(add(int(data[-1]), heap)) #иначе добавляем элемент в кучу
        elif int(data[0]) == 3: #третья операция
            if len(heap) >= int(data[-1]) and int(data[-1]) > 0: # проверка индекса по критериям
                result.append(direct_extract(int(data[-1]), heap)) #то удаляем элемент по индексу
            else:
                result.append(-1) #иначе -1 по условию

    for i in result: #вывод учитывая тип переменных
        if type(i) == tuple:
            print(*i)
        else:
            print(i)
    print(*heap)

main()