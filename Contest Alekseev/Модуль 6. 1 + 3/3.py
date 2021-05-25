class Heap(): #создаём класс
    def __init__(self, arr): #метод, при создании. self - аргумент, первое появление экземпляра
        self.__heap = arr

    @property
    def length(self):
        return len(self.__heap)


    def print_(self):
        print(*self.__heap)


    def shift_down(self, index):
        while 2*index+1 < self.length: #пока текущий индекс, с которым произвели умножение на 2 и сложение с 1 меньше, чем длина всего массива (кучи), присваиваем:
            left_index = 2*index+1 
            right_index = 2*index+2
            child_index = left_index
            if right_index < self.length and self.__heap[left_index] < self.__heap[right_index]: #если (правое текущее значение меньше, чем длина массива) и (куча[левый индекс] меньше куча[правый индекс]):
                child_index = right_index #child_index - дочерний индекс от родителя
            if self.__heap[child_index] <= self.__heap[index]:
                break
            self.__heap[index], self.__heap[child_index] = self.__heap[child_index], self.__heap[index] #меняем местами
            index = child_index

    def extract(self): #функция для извлечения 
        self.__heap[0], self.__heap[self.length-1] = self.__heap[self.length-1], self.__heap[0] #элемент для извленчения подходит здесь
        value=self.__heap.pop() #извлекается сюда
        self.shift_down(0)
        return value

def build_heap(arr):
    heap = arr[:]
    h = Heap(heap)
    for i in range(len(heap)-1, -1, -1):
        h.shift_down(i)
    return h

def main():
    n = int(input())
    list_ = list(map(int, input().split()))
    heap = build_heap(list_)
    res=[]
    while heap.length:
        heap.print_()
        res.insert(0,heap.extract())
    print(*res)
main()