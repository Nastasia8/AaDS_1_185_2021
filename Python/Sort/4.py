s = 0


def merge_sort(arr):
    global s
    if len(arr) > 1:
        left = arr[:len(arr)//2]
        right = arr[len(arr)//2:]
        merge_sort(left)
        merge_sort(right)

        r, l, k = 0, 0, 0
        while r < len(right) and l < len(left):  # Начиннаем объдинять части в один список
            if right[r] < left[l]:
                arr[k] = right[r]
                r += 1
                s += len(left)-l
            else:
                arr[k] = left[l]
                l += 1
            k += 1
        while l < len(left):  # Добавляем остатки литса в конец списка
            arr[k] = left[l]
            k += 1
            l += 1
        while r < len(right):  # Добавляем остатки листа в конец списка
            arr[k] = right[r]
            k += 1
            r += 1
    return arr


n = int(input())
arr = list(map(int, input().split()))[:n]
merge_sort(arr)
print(s)
# [print(item, end=' ')for item in arr]
