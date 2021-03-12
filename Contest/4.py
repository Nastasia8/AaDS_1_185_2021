

def merge_sort(arr):
    global count
    if len(arr) > 1:
        middle = len(arr) // 2
        half1 = arr[:middle]
        half2 = arr[middle:]
        merge_sort(half1)
        merge_sort(half2)
        i = 0
        j = 0
        k = 0
        while i < len(half1) and j < len(half2):
            if half1[i] > half2[j]:
                arr[k] = half2[j]
                j += 1
                count += len(half1) - i
            else:
                arr[k] = half1[i]
                i += 1
            k += 1

        while i < len(half1):
            arr[k] = half1[i]
            k += 1
            i += 1
            
        while j < len(half2):
            arr[k] = half2[j]
            k += 1
            j += 1
    return arr

n = int(input())
arr = list(map(int, input().split()))[:n]
count = 0
merge_sort(arr)
print(count)