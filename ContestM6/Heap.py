def build_heap(arr):
    heap = arr[:]
    for i in range(len(heap)-1, -1, -1):
        shift_down(i, heap)
    return heap

def shift_up(index, heap):
    while heap[index] < heap[(index-1)//2]:
        heap[index], heap[(index-1)//2] = heap[(index-1)//2], heap[index]
        index = (index-1)//2

def shift_down(index, heap):
    while 2*index+1 < len(heap):
        left_index = 2*index+1
        right_index = 2*index+2
        child_index = left_index
        if right_index < len(heap) and heap[left_index] > heap[right_index]:
            child_index = right_index
        if heap[child_index] >= heap[index]:
            break
        heap[index], heap[child_index] = heap[child_index], heap[index]
        index = child_index

def add(item, heap):
    heap.append(item)
    shift_up(len(heap)-1, heap)
    
def extract(heap):
    heap[0], heap[len(heap)-1] = heap[len(heap)-1], heap[0]
    heap.pop()
    shift_down(0, heap)

def get_min(heap):
    return heap[0]

def main():
    n = int(input())
    list_ = list(map(int, input().split()))
    heap = build_heap(list_)
    print(*heap)
    while len(heap):
        print(get_min(heap), end=" ")
        extract(heap)
main()  