"""
>>> import sys, io
>>> sys.stdin = io.StringIO(chr(10).join(['9', '12', '32', '45', '67', '98', '29', '61', '35', '09']))
>>> radix()
Initial array:
12, 32, 45, 67, 98, 29, 61, 35, 09
**********
Phase 1
Bucket 0: empty
Bucket 1: 61
Bucket 2: 12, 32
Bucket 3: empty
Bucket 4: empty
Bucket 5: 45, 35
Bucket 6: empty
Bucket 7: 67
Bucket 8: 98
Bucket 9: 29, 09
**********
Phase 2
Bucket 0: 09
Bucket 1: 12
Bucket 2: 29
Bucket 3: 32, 35
Bucket 4: 45
Bucket 5: empty
Bucket 6: 61, 67
Bucket 7: empty
Bucket 8: empty
Bucket 9: 98
**********
Sorted array:
09, 12, 29, 32, 35, 45, 61, 67, 98
"""


def radix():
    n = int(input())
    k, p = 0, 1
    k_max = 0
    arr = []
    for i in range(n):
        k = 0  # Заполняем список и считаем максимальное кол-во разрядов
        x = int(input())
        arr.append(x)
        if x == 0:
            k = 1
        while x != 0:
            x = x//10
            k += 1
        if k > k_max:
            k_max = k
    print('Initial array:')
    # [print(f'{arr[i]}, ', end="") for i in range(n)]
    for i in range(n):  # Уравниваем разряды
        k = 0
        m = arr[i]
        if arr[i] == 0:
            k = 1
        while m != 0:
            m = m//10
            k += 1
        arr[i] = f'{arr[i]}'
        for j in range(k_max-k):
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
        for i in range(10):
            if arr_index[i] != []:
                print(f'Bucket {i}: ', end="")
                for x in range(len(arr_index[i])):
                    if x != len(arr_index[i])-1:
                        print(f'{arr_index[i][x]}, ', end="")
                    else:
                        print(arr_index[i][x])
            else:
                print(f'Bucket {i}: empty')
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


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
