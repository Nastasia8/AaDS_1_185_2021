def merge_sort(arr, begin_, end_):
    if len(arr) > 1:
        left = arr[:len(arr)//2]
        right = arr[len(arr)//2:]
        if len(arr) % 2 == 0:
            merge_sort(left, begin_, end_-len(arr)//2)
        else:
            merge_sort(left, begin_, end_-len(arr)//2-1)
        merge_sort(right, begin_+len(arr)//2, end_)

        r, l, k = 0, 0, 0
        while r < len(right) and l < len(left):  # Начиннаем объдинять части в один список
            if right[r] < left[l]:
                arr[k] = right[r]
                r += 1
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
        print(begin_, end_, arr[0], arr[-1])
    return arr


n = int(input())
arr = list(map(int, input().split()))[:n]
merge_sort(arr, 1, len(arr))
[print(item, end=' ')for item in arr]
