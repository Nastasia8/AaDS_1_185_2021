

# #Values are fine, i need to only calculate indexes of merge
def merge_sort(arr):
    if len(arr) > 1:
        global arr_copy
        middle = len(arr) // 2
        half1 = arr[:middle]
        half2 = arr[middle:]
        #recursion
        merge_sort(half1)
        merge_sort(half2)
        i, j, k = 0, 0, 0
        #Здесь сравниваются две половины и, если первая больше второй, меняется местами.
        #Пока длина первой>i и второй>j
        while i < len(half1) and j < len(half2):
            #Если элемент первой половины меньше элемента второй половины, то эл. первой становится вперёд
            if half1[i] < half2[j]:
                arr_copy[arr_copy.index(half2[j])], arr_copy[arr_copy.index(half1[i])] = half1[i], half2[j]
                print(arr_copy[arr_copy.index(half2[j])], arr_copy[arr_copy.index(half1[i])], "swapped:", half1[i], half2[j])
                arr[k] = half1[i]
                i += 1
            #Иначе, эл. второй становится вперед
            elif half1[i] > half2[j]:
                arr_copy[arr_copy.index(half1[i])], arr_copy[arr_copy.index(half2[j])] = half2[j], half1[i]
                print(arr_copy[arr_copy.index(half1[i])], arr_copy[arr_copy.index(half2[j])], "swapped:", half2[j], half1[i])
                arr[k] = half2[j]
                j += 1
            else:
                i += 1
                j += 1
            k += 1
        #Здесь происходит слияние первого списка в основной arr
        while i < len(half1):
            arr[k] = half1[i]
            k += 1
            i += 1
        #Здесь происходит слияние второго списка в основной arr
        while j < len(half2):
            arr[k] = half2[j]
            k += 1
            j += 1
        id1 = arr_copy.index(arr[0])+1
        id2 = arr_copy.index(arr[-1])+1
        print(id1, id2, arr[0], arr[-1])
    return arr


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))[:n]
    arr_copy = arr.copy()
    if n == 1:
        print(arr[0])
    else:
        merge_sort(arr)
        [print(i, end=" ") for i in arr]



