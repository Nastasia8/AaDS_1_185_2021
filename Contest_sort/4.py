count=0
def merge_sort(numbers, start,end):
    if (end - start > 1):
        middle = (start + end) // 2
        merge_sort(numbers, start, middle)
        merge_sort(numbers, middle, end)
        left = numbers [start: middle]
        right = numbers[middle: end]
        merge_list(numbers, left, right, start)
        
def merge_list(Array, left, right, start):
    global count
    i = j = 0 
    K = start
    while i < len(right) and j < len(left):
        if left[j] > right[i]:
            Array[K] = right[i]
            i += 1
            count += len(left)-j
        else:
            Array[K] = left[j]
            j += 1
        K += 1
    while j < len(left):
        Array [K] = left[j]
        j += 1
        K += 1
    while i < len(right):
        Array[K] = right[i]
        i += 1
        K += 1        

def main ():
    n = int(input())
    Array = list(map(int, input().split(maxsplit = n)))
    merge_sort(Array, 0, len(Array))
    print (count)

main()
