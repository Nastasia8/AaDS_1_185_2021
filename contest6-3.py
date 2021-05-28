def build_bh(arr):
    heap_ = arr[:]
    for i in range(len(heap_)-1, -1, -1):
        shift_down(i, heap_)
    return heap_

def shift_up(c, heap_):
    while heap_[c] > heap_[(c-1)//2]:
        heap_[c], heap_[(c-1)//2] = heap_[(c-1)//2], heap_[c]
        c = (c-1)//2
def shift_down(c, heap_):
    while 2*c+1 < len(heap_):
        left = 2*c+1
        right = 2*c+2
        child = left
        if  right < len(heap_) and heap_[left] < heap_[right]:
            child = right
        if heap_[child] <= heap_[c]:
            break
        heap_[c], heap_[child] = heap_[child], heap_[c]
        c = child
def add(item, heap_):
    heap_.append(item)
    shift_up(len(heap_)-1, heap_)
def extract(heap_):
    global srt_heap
    heap_[0], heap_[len(heap_)-1] = heap_[len(heap_)-1], heap_[0]
    srt_heap.append(heap_.pop())
    shift_down(0, heap_)

def get_min(heap_):
    return heap_[0]


n = int(input())
s = list(map(int, input().split()))[:n]
heap = build_bh(s)
srt_heap = []
while len(heap):
    print(*heap)
    extract(heap)
print(*srt_heap[::-1])
