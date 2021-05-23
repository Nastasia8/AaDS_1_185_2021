
def shift_up(index, heap):
    while heap[index] > heap[(index-1)//2]:
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

    
def extract(heap):
    heap[0], heap[len(heap)-1] = heap[len(heap)-1], heap[0]
    ind = heap.pop()
    return shift_down(0, heap), ind

def get_max(heap):
    return heap[0]

def main():
    heap = []
    result = []
    input_ = input().split()
    n, m = int(input_[0]), int(input_[1])
    for i in range(1, m+1):
        data = input()
        if int(data[0]) == 1:
            if not heap:
                result.append(-1)
                #print(-1)
            else:
                #print(extract(heap))
                result.append(extract(heap))
        elif int(data[0]) == 2:
            if len(heap) == n:
                #print(-1)
                result.append(-1)
            else:
                #print(add(int(data[-1]), heap))
                result.append(add(int(data[-1]), heap))
    for i in result:
        if type(i) == tuple:
            print(*i)
        else:
            print(i)
    print(*heap)

main()