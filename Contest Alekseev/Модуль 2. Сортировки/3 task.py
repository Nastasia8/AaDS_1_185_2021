def mergeSort(numbers, start, end):
    if end - start > 1:
        middle = (start + end) // 2
        mergeSort(numbers, start, middle)
        mergeSort(numbers, middle, end)
        left = numbers[start: middle]
        right = numbers[middle: end]
        internalSort(numbers, left, right, start)
        print(start + 1, end, numbers[start], numbers[end - 1])

def internalSort(arr, left, right, start):
    a = j = 0
    g = start
    while a < len(right) and j < len(left):
        if left[j] > right[a]:
            arr[g] = right[a]
            a +=1
        else:
            arr[g] = left[j]
            j += 1
        g += 1
    while j < len(left):
        arr[g] = left[j]
        j += 1
        g += 1
    while a < len(right):
        arr[g] = right[a]
        a += 1
        g += 1

def main():
    m = int(input())
    numbers = list(map(int,input().split(maxsplit = m)))
    mergeSort(numbers, 0, len(numbers))
    print(*numbers)

main()