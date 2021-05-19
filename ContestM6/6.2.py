class Heap:
    __heap = []
        
    @property
    def length(self):
        return len(self.__heap)
        
    @property
    def empty(self):
        return self.length == 0
        
    @property
    def min(self):
        return self.__heap[0]
        
    def clear(self):
        return self.__heap.clear()
        
    def shift_down(self, value):
        while 2*value+1 < self.length:
            left_indx = 2*value+1
            right_indx = 2*value+2
            _indx = left_indx
            if right_indx < self.length and self.__heap[left_indx] > self.__heap[right_indx]:
                _indx = right_indx
            if self.__heap[_indx] >= self.__heap[value]:
                break
            self.__heap[value], self.__heap[_indx] = self.__heap[_indx], self.__heap[value]
            value = _indx
    
    def shift_up(self, value):
        while value > 0 and self.__heap[value] < self.__heap[(value - 1)//2]:
            self.__heap[value],self.__heap[(value - 1)//2] = self.__heap[(value - 1)//2], self.__heap[value]
            value = (value - 1)//2
    
    def extract(self):
        self.__heap[0], self.__heap[self.length-1] = self.__heap[self.length-1], self.__heap[0]
        self.__heap.pop()
        self.shift_down(0)
    
    def add(self, value):
        self.__heap.append(value)
        self.shift_up(self.length-1)
    
    def print_heap(self):
        print(*self.__heap)

def build(arr):
    heap = arr[:]
    h = Heap(heap)
    for i in range(len(heap)-1, -1, -1):
        h.shift_down(i)
    return h

def main():
    n = int(input())
    res = []
    heap = Heap()
    for i in range(n):
        command = list(map(str, input().split()))
        if command[0] == "ADD":
           heap.add(int(command[1])) 
        elif command[0] == "CLEAR":
            heap.clear()
        else:
            if heap.empty:
                res.append("CANNOT")
            else:
                res.append(heap.min)
                heap.extract()
            
    print(*res, sep="\n")
    
main()
'''
ADD 192168812
ADD 125
ADD 321
EXTRACT
EXTRACT
CLEAR
ADD 7
ADD 555
EXTRACT
EXTRACT
EXTRACT
'''
