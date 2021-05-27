def shift_up(index, heap):#
    while heap[index] > heap[(index-1)//2] and (index-1)//2 >= 0:
        heap[index], heap[(index-1)//2] = heap[(index-1)//2], heap[index]
        index = (index-1)//2
    return index+1

def shift_down(index, heap):#
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

def add(item, heap):#функция добавления элемента в дерево
    heap.append(item)
    return shift_up(len(heap)-1, heap)

    
def extract(heap): #функция извлечения элемента из дерева
    heap[0], heap[len(heap)-1] = heap[len(heap)-1], heap[0] #первый и последний элементы меняются местами
    ind = heap.pop()#в индексе запоминаем последний элемент кучи
    if heap:
        return shift_down(0, heap), ind#если есть куча, то возвращаем сдвинутый вниз элемент и последний элемент
    else:
        return 0, ind#возвращается ноль и индекс

def get_max(heap):#получаем верхний элемент, максимум
    return heap[0]

def main():
    heap = []
    result = []
    input_ = input().split()
    n, m = int(input_[0]), int(input_[1])#ввод 2х переменных в строчку
    for i in range(m):#
        data = input().split()
        if int(data[0]) == 1:#узнаём номер команды
            if not heap:
                result.append(-1)
            else:
                result.append(extract(heap))#в результат добавляем извлеченный элемент
        elif int(data[0]) == 2:#узнаём номер команды
            if len(heap) == n:
                result.append(-1)
            else:
                result.append(add(int(data[-1]), heap))#добавляем последний элемент
    for i in result:# для каэдого элемтав результате, если список то вывести без знаков, если переменнаято обычный вывод
        if type(i) == tuple:
            print(*i)
        else:
            print(i)
    print(*heap)#вывод кучи

main()
