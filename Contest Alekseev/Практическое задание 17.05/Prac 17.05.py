def build_heap(arr):
    heap = arr[:]
    for i in range((len(heap)-1), -1, -1):
        shift_down(i, heap)
    return heap
        
def shift_up(current_indx, heap):
    while heap[current_indx] < heap[(current_indx-1)//2]:
        heap[current_indx], heap[(current_indx-1)//2] = heap[(current_indx-1)//2], heap[current_indx]
        current_indx = (current_indx-1)//2
        
def shift_down(current_indx, heap):
    while 2*current_indx+1 < len(heap):
        left_indx = 2*current_indx+1
        right_indx = 2*current_indx+2
        child_indx = left_indx
        if (right_indx < len(heap)) and (heap[left_indx] > heap[right_indx]):
            child_indx = right_indx
        if heap[child_indx] >= heap[current_indx]:
            break
        heap[current_indx], heap[child_indx] = heap[child_indx], heap[current_indx]
        current_indx = child_indx
        
def get_min(heap):
    return (heap[0])

def add(element, heap):
    heap.append(element)
    shift_up(len(heap)-1, heap)

def extract(heap):
    heap[0], heap[len(heap)-1] = heap[len(heap)-1], heap[0]
    heap.pop()
    shift_down(0, heap)    
    
def main():
    n = int(input())
    a = list(map(int, input().split()))[:n]
    heap = build_heap(a)
    print(*heap)
    while len(heap):
        print(get_min(heap), end=" ")
        extract(heap)
main()
    