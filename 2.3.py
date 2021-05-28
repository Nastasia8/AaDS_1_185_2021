def radix():
    n = int(input())
    k, p = 0, 1
    k_max = 0
    arr = []
    for i in range(n):
        k = 0  # Заполняем список и считаем максимальное кол-во разрядов
        x = str(input())
        arr.append(x)
        for item in arr:
            if len(item) > k_max:
                k_max = len(item)
    print('Initial array:')
    for i in range(n):  # Уравниваем разряды
        if len(arr[i]) < k_max:
            while len(arr[i]) != k_max:
                arr[i] = f'0{arr[i]}'
    for i in range(n):
        if i == n-1:
            print(arr[i])
        else:
            print(f'{arr[i]}, ', end="")
    print('**********')
    arr_index = [[] for i in range(10)]
    for i in range(k_max-1, -1, -1):  # Заполняем arr_index
        print(f'Phase {p}')
        p += 1
        for j in range(n):
            for f in range(10):
                if arr[j][i] == str(f):
                    arr_index[f].append(arr[j])
        for l in range(10):
            if arr_index[l] != []:
                print(f'Bucket {l}: ', end="")
                for x in range(len(arr_index[l])):
                    if x != len(arr_index[l])-1:
                        print(f'{arr_index[l][x]}, ', end="")
                    else:
                        print(arr_index[l][x])
            else:
                print(f'Bucket {l}: empty')
        print('**********')
        arr.clear()
        for i in range(10):  # переписываем arr
            while arr_index[i] != []:
                arr.append(arr_index[i].pop(0))

    print("Sorted array:")
    for i in range(n):
        if i == n-1:
            print(arr[i])
        else:
            print(f'{arr[i]}, ', end="")


radix()