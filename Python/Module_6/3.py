from collections import deque


class Heap:
    def __init__(self, arr):
        self.__heap = arr

    @property
    def lenght(self):
        return len(self.__heap)

    def shift_down(self, value):
        while 2*value+1 < len(self.__heap):
            left_cur_index = 2*value+1
            right_cur_index = 2*value+2
            child_index = left_cur_index
            if right_cur_index < len(self.__heap) and self.__heap[left_cur_index] < self.__heap[right_cur_index]:
                child_index = right_cur_index
            if self.__heap[child_index] <= self.__heap[value]:
                break
            self.__heap[child_index], self.__heap[value] = self.__heap[value], self.__heap[child_index]
            value = child_index

    @property
    def extract_and_get_max(self):
        self.__heap[0], self.__heap[len(
            self.__heap) - 1] = self.__heap[len(self.__heap)-1], self.__heap[0]
        x = self.__heap.pop()
        self.shift_down(0)
        return x

    @property
    def get_min(self):
        return self.__heap[0]

    @property
    def print_heap(self):
        print(*self.__heap)


def built(arr):
    heap = arr[:]
    h = Heap(heap)
    for i in range(len(heap)-1, -1, -1):
        h.shift_down(i)
    return h


def main():
    n = int(input())
    arr = [int(i) for i in input().split()]
    heap = built(arr)
    result = deque()
    while heap.lenght:
        heap.print_heap
        result.appendleft(heap.extract_and_get_max)
    print(*result)


main()
