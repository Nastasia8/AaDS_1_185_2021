#Задание в целом делали на паре. С циклом while вы дали подсказку) 
#Это задание делал
class Heap():
    def __init__(self, arr):
        self.__heap = arr

    @property
    def length(self):
        return len(self.__heap)


    def print_(self):
        print(*self.__heap)


    def shift_down(self, index):
        while 2*index+1 < self.length:
            left_index = 2*index+1
            right_index = 2*index+2
            child_index = left_index
            if right_index < self.length and self.__heap[left_index] < self.__heap[right_index]:
                child_index = right_index
            if self.__heap[child_index] <= self.__heap[index]:
                break
            self.__heap[index], self.__heap[child_index] = self.__heap[child_index], self.__heap[index]
            index = child_index

    def extract(self):
        self.__heap[0], self.__heap[self.length-1] = self.__heap[self.length-1], self.__heap[0]
        value=self.__heap.pop()
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
    nums = list(map(int, input().split()))[:n]
    heap = build_heap(nums)
    result=[]
    while heap.length:
        heap.print_()
        result.insert(0,heap.extract())
    print(*result)
main()