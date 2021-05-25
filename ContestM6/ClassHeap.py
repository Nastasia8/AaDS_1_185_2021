

class Heap():
    def __init__(self, arr):
        self.__heap = arr
        
    @property
    def length(self):
        return len(self.__heap)

    @property
    def empty(self):
        return self.length == 0

    @property
    def minimum(self):
        return self.__heap[0]

    def print_(self):
        print(*self.__heap)

    def shift_up(self, index):
        while self.__heap[index] < self.__heap[(index-1)//2]:
            self.__heap[index], self.__heap[(index-1)//2] = self.__heap[(index-1)//2], self.__heap[index]
            index = (index-1)//2

    def shift_down(self, index):
        while 2*index+1 < self.length:
            left_index = 2*index+1
            right_index = 2*index+2
            child_index = left_index
            if right_index < self.length and self.__heap[left_index] > self.__heap[right_index]:
                child_index = right_index
            if self.__heap[child_index] >= self.__heap[index]:
                break
            self.__heap[index], self.__heap[child_index] = self.__heap[child_index], self.__heap[index]
            index = child_index

    def add(self, item):
        self.__heap.append(item)
        self.shift_up(self.length)
        
    def extract(self):
        self.__heap[0], self.__heap[self.length-1] = self.__heap[self.length-1], self.__heap[0]
        self.__heap.pop()
        self.shift_down(0)

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
    heap.print_()
    while heap.length:
        print(heap.minimum, end=" ")
        heap.extract()
main()  