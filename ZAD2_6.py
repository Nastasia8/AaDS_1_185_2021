def shift_up(index, heap):
    while heap[index] > heap[(index-1)//2] and (index-1)//2 >= 0:
        heap[index], heap[(index-1)//2] = heap[(index-1)//2], heap[index]
        index = (index-1)//2
    return index+1#функция перемещает массив вверх,пока он снава не станет кучей и добавляется индекс 

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
    return index+1#функция проверяет массив и перемещает нужное число как можно дальше вниз


def add(item, heap):
    heap.append(item)
    return shift_up(len(heap)-1, heap)#создание нового числа 

def direct_extract(index, heap):
    val = heap[len(heap)-1]
    heap[index-1], heap[len(heap)-1] = heap[len(heap)-1], heap[index-1]
    ind = heap.pop()
    if val < ind:
        shift_down(index-1, heap)
    elif val > ind:
        shift_up(index-1, heap)
    return ind#элемент индекс которого мы задали удаляется 

def extract(heap):
    heap[0], heap[len(heap)-1] = heap[len(heap)-1], heap[0]
    ind = heap.pop()
    if heap:
        return shift_down(0, heap), ind
    else:
        return 0, ind#находит максимальное и извлекает его

def get_max(heap):
    return heap[0]#максимальный элемент

def main():#ввод и вывод всех элементов 
    heap = []
    result = []
    input_ = input().split()
    n, m = int(input_[0]), int(input_[1])
    for i in range(m):
        data = input().split()
        if int(data[0]) == 1:#если дерево пустое ты выводиться -1
            if not heap:
                result.append(-1)
            else:
                result.append(extract(heap))
        elif int(data[0]) == 2:#если нельзя добавить новый элемент, то -1
            if len(heap) == n:
                result.append(-1)
            else:
                result.append(add(int(data[-1]), heap))
        elif int(data[0]) == 3:
            if len(heap) >= int(data[-1]) and int(data[-1]) > 0:
                result.append(direct_extract(int(data[-1]), heap))
            else:
                result.append(-1)

    for i in result:
        if type(i) == tuple:
            print(*i)
        else:
            print(i)
    print(*heap)

main()