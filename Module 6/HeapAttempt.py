from heapq import heappop, heappush

def buildTree():
    pass

def shiftUp(heap):
    pass

def shiftDown(heap):
    pass

def main():
    n = int(input())
    heap = []
    result = []
    for i in range(n):
        command = list(map(str, input().split()))
        if command[0] == "ADD":
            heappush(heap, -int(command[1]))
        elif command[0] == "EXTRACT":
            if not heap:
                result.append("CANNOT")
            else:
                result.append(-heappop(heap))
        else:
            heap.clear()
    print(*result)

main()