def inv(massiv, c):#функция для нахождения инверсий
    if len(M) > 1:#если длина больше 1
        mid = len(massiv)//2
        left = massiv[:mid]#делим на правую и левую части
        right = massiv[mid:]
        
        c = inv(left, c)
        c = inv(right, c)

        i,j,k = 0,0,0
        while i < len(left) and j < len(right):# пока счетчики меньше длины частей
            if left[i] <= right[j]:
                massiv[k] = left[i]#замена значения если меньше или равно, аналогично для других случаев
                i += 1
            else:
                massiv[k] = right[j]
                j = j+1
                c += len(left)-i
            k = k+1
        while i < len(left):
            massiv[k] = left[i]
            i = i+1
            k = k+1
        while j < len(right):
            massiv[k] = right[j]
            j = j+1
            k = k+1
    return c
invers = 0
n = int(input())#ввод
M = list(map(int, input().split()))[:n]
invers = inv(M, invers)
print(invers)