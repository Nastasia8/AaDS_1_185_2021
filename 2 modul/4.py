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
    a = g = 0 
    K = start
    while a < len(right) and g < len(left):
        if left[g] > right[a]:
            Array[K] = right[a]
            a += 1
            count += len(left)-g
        else:
            Array[K] = left[g]
            g += 1
        K += 1
    while g < len(left):
        Array [K] = left[g]
        g += 1
        K += 1
    while a < len(right):
        Array[K] = right[a]
        a += 1
        K += 1        

def main ():
    n = int(input())
    Array = list(map(int, input().split(maxsplit = n)))
    merge_sort(Array, 0, len(Array))
    print (count)